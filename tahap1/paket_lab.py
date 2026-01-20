import mysql.connector # type: ignore

db_awal = mysql.connector.connect(
    host="localhost",
    user="eric",
    password="eric123",
    database="db_slims"
)

db_tujuan = mysql.connector.connect(
    host="localhost",
    user="eric",
    password="eric123",
    database="db_slims_marinir_aio"
)

cursor_awal = db_awal.cursor(dictionary=True)
cursor_tujuan = db_tujuan.cursor()

cursor_awal.execute("SELECT * FROM paket_lab")
data_awal = cursor_awal.fetchall()

for row in data_awal:
    try:


        query = """
            INSERT INTO paket_lab (
                id_paket_lab, nama_paket, lokasi_pemeriksaan, keterangan, harga, 
                kode_his, no_jenis, status, 
                id_user, user_update, created_at, updated_at
            ) VALUES (
                %(id_paket_lab)s, %(nama_paket)s, %(lokasi_pemeriksaan)s, %(keterangan)s, %(harga)s, 
                %(kode_his)s, %(no_jenis)s, %(status)s, 
                %(id_user)s, %(user_update)s, %(created_at)s, %(updated_at)s
            )
        """
        cursor_tujuan.execute(query, row)
    except Exception as e:
        print(f"Gagal insert ID {row.get('id_paket_lab ', 'UNKNOWN')}: {e}")

db_tujuan.commit()
print("Selesai memindahkan data paket_lab.")
