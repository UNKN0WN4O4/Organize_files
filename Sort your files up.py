import os
import shutil
from pathlib import Path
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import threading


FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.tiff', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.md', '.odt', '.rtf'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.m4v'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
    'Programs': ['.exe', '.msi', '.apk', '.dmg', '.deb', '.rpm'],
    'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.sql', '.json', '.xml'],
    'Others': []
}

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer & Cleaner")
        self.root.geometry("600x450")
        self.selected_folder = None
        
   
        header = tb.Label(
            root, 
            text="📁 File Organizer & Cleaner", 
            font=('Segoe UI', 18, 'bold'),
            bootstyle="primary"
        )
        header.pack(pady=20)
        
      
        folder_frame = tb.Frame(root)
        folder_frame.pack(pady=10, padx=20, fill=X)
        
        self.folder_label = tb.Label(
            folder_frame, 
            text="No folder selected", 
            font=('Segoe UI', 10),
            bootstyle="secondary"
        )
        self.folder_label.pack(side=LEFT, padx=5)
        
        browse_btn = tb.Button(
            folder_frame,
            text="Browse Folder",
            command=self.browse_folder,
            bootstyle="info"
        )
        browse_btn.pack(side=RIGHT, padx=5)
        
        # Options frame
        options_frame = tb.LabelFrame(root, text="Organization Options", padding=15)
        options_frame.pack(pady=15, padx=20, fill=BOTH, expand=True)
        
        # Organize by type button
        type_btn = tb.Button(
            options_frame,
            text="📂 Organize by File Type",
            command=self.organize_by_type,
            bootstyle="success-outline",
            width=30
        )
        type_btn.pack(pady=8)
        
        # Organize by size button
        size_btn = tb.Button(
            options_frame,
            text="📊 Organize by File Size",
            command=self.organize_by_size,
            bootstyle="warning-outline",
            width=30
        )
        size_btn.pack(pady=8)
        
        # Clean empty folders button
        clean_btn = tb.Button(
            options_frame,
            text="🗑️ Clean Empty Folders",
            command=self.clean_empty_folders,
            bootstyle="danger-outline",
            width=30
        )
        clean_btn.pack(pady=8)
        
        # Status/Progress area
        self.status_text = tb.Text(
            root,
            height=8,
            width=70,
            font=('Consolas', 9),
            wrap=WORD
        )
        self.status_text.pack(pady=10, padx=20)
        
        # Footer
        footer = tb.Label(
            root,
            text="Made with Python & ttkbootstrap",
            font=('Segoe UI', 8),
            bootstyle="secondary"
        )
        footer.pack(pady=5)
    
    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder to Organize")
        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=f"Selected: {folder}")
            self.log(f"✅ Folder selected: {folder}\n")
    
    def log(self, message):
        self.status_text.insert(END, message)
        self.status_text.see(END)
        self.root.update()
    
    def organize_by_type(self):
        if not self.selected_folder:
            messagebox.showwarning("No Folder", "Please select a folder first!")
            return
        
        self.status_text.delete(1.0, END)
        self.log("🔄 Organizing by file type...\n")
        threading.Thread(target=self._organize_by_type_thread, daemon=True).start()
    
    def _organize_by_type_thread(self):
        folder = Path(self.selected_folder)
        files_moved = 0
        
        for item in folder.iterdir():
            if item.is_file():
                file_ext = item.suffix.lower()
                
                category = 'Others'
                for cat, extensions in FILE_CATEGORIES.items():
                    if file_ext in extensions:
                        category = cat
                        break
                
                category_folder = folder / category
                category_folder.mkdir(exist_ok=True)
                
                destination = category_folder / item.name
                
                if destination.exists():
                    base_name = item.stem
                    counter = 1
                    while destination.exists():
                        new_name = f"{base_name}_{counter}{file_ext}"
                        destination = category_folder / new_name
                        counter += 1
                
                try:
                    shutil.move(str(item), str(destination))
                    self.log(f"✓ {item.name} → {category}/\n")
                    files_moved += 1
                except Exception as e:
                    self.log(f"✗ Error: {item.name} - {e}\n")
        
        self.log(f"\n✅ Done! {files_moved} files organized.\n")
        messagebox.showinfo("Success", f"Organized {files_moved} files by type!")
    
    def organize_by_size(self):
        if not self.selected_folder:
            messagebox.showwarning("No Folder", "Please select a folder first!")
            return
        
        self.status_text.delete(1.0, END)
        self.log("🔄 Organizing by file size...\n")
        threading.Thread(target=self._organize_by_size_thread, daemon=True).start()
    
    def _organize_by_size_thread(self):
        folder = Path(self.selected_folder)
        files_moved = 0
        
        for item in folder.iterdir():
            if item.is_file():
                file_size_mb = item.stat().st_size / (1024 * 1024)
                
                if file_size_mb < 1:
                    size_category = "Small"
                elif file_size_mb < 50:
                    size_category = "Medium"
                else:
                    size_category = "Large"
                
                size_folder = folder / size_category
                size_folder.mkdir(exist_ok=True)
                
                destination = size_folder / item.name
                
                if destination.exists():
                    base_name = item.stem
                    ext = item.suffix
                    counter = 1
                    while destination.exists():
                        new_name = f"{base_name}_{counter}{ext}"
                        destination = size_folder / new_name
                        counter += 1
                
                try:
                    shutil.move(str(item), str(destination))
                    self.log(f"✓ {item.name} ({file_size_mb:.2f} MB) → {size_category}/\n")
                    files_moved += 1
                except Exception as e:
                    self.log(f"✗ Error: {item.name} - {e}\n")
        
        self.log(f"\n✅ Done! {files_moved} files organized.\n")
        messagebox.showinfo("Success", f"Organized {files_moved} files by size!")
    
    def clean_empty_folders(self):
        if not self.selected_folder:
            messagebox.showwarning("No Folder", "Please select a folder first!")
            return
        
        self.status_text.delete(1.0, END)
        self.log("🔄 Cleaning empty folders...\n")
        threading.Thread(target=self._clean_empty_thread, daemon=True).start()
    
    def _clean_empty_thread(self):
        folder = Path(self.selected_folder)
        removed = 0
        
        for item in folder.iterdir():
            if item.is_dir() and not any(item.iterdir()):
                try:
                    item.rmdir()
                    self.log(f"✓ Removed: {item.name}\n")
                    removed += 1
                except Exception as e:
                    self.log(f"✗ Error: {item.name} - {e}\n")
        
        self.log(f"\n✅ Done! {removed} empty folders removed.\n")
        messagebox.showinfo("Success", f"Removed {removed} empty folders!")

if __name__ == "__main__":
    root = tb.Window(themename="flatly")
    app = FileOrganizerApp(root)
    root.mainloop()
