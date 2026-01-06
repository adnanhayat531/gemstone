
import os
import shutil

# Artifacts directory where images were generated
source_dir = r"C:\Users\adnan.h\.gemini\antigravity\brain\a8715e1f-6884-4120-b677-043b2731f306"

# Destination directory (MEDIA_ROOT/gemstones)
dest_dir = r"c:\Users\adnan.h\Desktop\projects\gemstone\media\gemstones"

# Create destination if not exists
os.makedirs(dest_dir, exist_ok=True)

start_path = os.getcwd() # just to know where we are
print(f"Current WD: {start_path}")

files_to_copy = {
    "ruby_gemstone_1767663595437.png": "ruby.png",
    "sapphire_gemstone_1767663615194.png": "sapphire.png",
    "emerald_gemstone_1767663632249.png": "emerald.png",
    "diamond_gemstone_1767663649414.png": "diamond.png",
    "amethyst_gemstone_1767663665122.png": "amethyst.png"
}

success_count = 0

print(f"Copying files from {source_dir} to {dest_dir}...")

for src_name, dest_name in files_to_copy.items():
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    
    if os.path.exists(src_path):
        try:
            shutil.copy2(src_path, dest_path)
            print(f"SUCCESS: Copied {src_name} -> {dest_name}")
            success_count += 1
        except Exception as e:
            print(f"ERROR: Failed to copy {src_name}: {e}")
    else:
        print(f"WARNING: Source file not found: {src_path}")

print(f"Finished. Copied {success_count}/{len(files_to_copy)} files.")
