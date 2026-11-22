import argparse
import shutil
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".md", ".odt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".xz"],
    "Installers": [".rpm", ".deb", ".appimage", ".iso", ".exe", ".run"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".json", ".sh", ".sql"],
}


def get_default_downloads() -> Path:
    """Mendeteksi otomatis folder ~/Unduhan atau ~/Downloads."""
    unduhan = Path.home() / "Unduhan"
    if unduhan.exists():
        return unduhan
    return Path.home() / "Downloads"


def get_target_folder_name(extension: str, mode: str) -> str:
    """Menentukan nama folder tujuan berdasarkan mode (category atau ext)."""
    ext = extension.lower()
    if mode == "ext":
        return ext.lstrip(".") if ext else "no_extension"

    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def get_unique_destination(dest_folder: Path, filename: str) -> Path:
    """Menghindari file tertimpa dengan menambahkan angka jika nama sudah ada."""
    dest_path = dest_folder / filename
    if not dest_path.exists():
        return dest_path

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_dest = dest_folder / new_name
        if not new_dest.exists():
            return new_dest
        counter += 1


def organize_folder(target_dir: Path, mode: str = "ext", dry_run: bool = False):
    """Memindai dan memindahkan file di dalam folder target."""
    if not target_dir.exists() or not target_dir.is_dir():
        console.print(f"[bold red]Error:[/bold red] Folder '{target_dir}' tidak ditemukan.")
        return

    status_mode = "[yellow]DRY-RUN (Simulasi)[/yellow]" if dry_run else "[green]LIVE (Eksekusi)[/green]"
    console.print(
        Panel(
            f"📂 Folder Target : [bold cyan]{target_dir}[/bold cyan]\n"
            f"🗂️  Mode Sortir   : [bold magenta]{mode.upper()}[/bold magenta]\n"
            f"⚙️  Eksekusi      : {status_mode}",
            expand=False,
        )
    )

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Nama File", style="white", no_wrap=True, max_width=40)
    table.add_column("Folder Tujuan", style="cyan")
    table.add_column("Status", style="green")

    moved_count = 0

    for item in sorted(target_dir.iterdir()):
        if item.is_dir() or item.name.startswith("."):
            continue

        folder_name = get_target_folder_name(item.suffix, mode)
        dest_folder = target_dir / folder_name
        final_dest = get_unique_destination(dest_folder, item.name)

        if dry_run:
            status = f"Akan dipindah -> {folder_name}/{final_dest.name}"
        else:
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(final_dest))
            status = f"✔ Dipindah -> {folder_name}/{final_dest.name}"

        table.add_row(item.name, folder_name, status)
        moved_count += 1

    if moved_count == 0:
        console.print("\n[bold green]✨ Folder sudah rapi! Tidak ada file yang perlu dipindahkan.[/bold green]")
    else:
        console.print(table)
        summary = "file siap dipindahkan." if dry_run else "file berhasil dirapikan!"
        console.print(f"\n[bold]Total:[/bold] {moved_count} {summary}")


def main():
    parser = argparse.ArgumentParser(
        description="Sortify - Smart Downloads Organizer untuk merapikan folder secara otomatis."
    )
    parser.add_argument(
        "-p", "--path",
        type=str,
        default=str(get_default_downloads()),
        help="Path folder target (bawaan: ~/Unduhan atau ~/Downloads)",
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["ext", "category"],
        default="ext",
        help="Mode pengelompokan: 'ext' (berdasarkan ekstensi seperti pdf/docx) atau 'category' (Documents/Images)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulasikan pemindahan file tanpa mengubah isi folder",
    )

    args = parser.parse_args()
    target_path = Path(args.path).expanduser().resolve()
    organize_folder(target_path, mode=args.mode, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
