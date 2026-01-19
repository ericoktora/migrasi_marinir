import subprocess

# Daftar file python yang ingin dijalankan
scripts = [
    "kode_lab.py",
    "kode_lab_dt.py",
    "kode_lab_hsl.py",
    "jenis.py",
    "dokter.py",
    "dokter_pj.py",
    "grub.py",
    "grub_detail.py",
    "kategori_alat.py",
    "kategori_alat_detail.py",
    "kategori_catatan.py",
    "konten_ctt.py",
    "kritis.py",
    "kritis_dt.py",
    "paket_lab.py",
    "paket_lab_dt.py",
    "stt_assur.py",
    "users.py",
    "waktu_pmr.py",
    "printer.py",
    "printer_dt.py",
    "query_tahap_1.py",
]

for script in scripts:
    print(f"\n🚀 Menjalankan: {script}")
    result = subprocess.run(["python3", script])
    
    if result.returncode != 0:
        print(f"❌ Gagal menjalankan {script}, hentikan proses.")
        break
    else:
        print(f"✅ Selesai: {script}")
