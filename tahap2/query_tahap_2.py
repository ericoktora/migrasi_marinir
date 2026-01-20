import mysql.connector # type: ignore

conn = mysql.connector.connect(
    host="localhost",
    user="eric",
    password="eric123",
    database="db_slims_marinir_aio"
)

cursor = conn.cursor()

# Jalankan semua query
try:
    


    cursor.execute("UPDATE transaksi_lab set id_asal = 1;")

    cursor.execute("UPDATE transaksi_lab set id_cara_masuk = 1;")

    cursor.execute("UPDATE transaksi_lab SET id_petugas_lab = id_petugas_lab + 100;")

    cursor.execute("""
        UPDATE transaksi_lab
        SET id_petugas_lab = CASE
            WHEN id_petugas_lab = 100 THEN 42 
            WHEN id_petugas_lab = 114 THEN 23 
            WHEN id_petugas_lab = 115 THEN 24  
            WHEN id_petugas_lab = 116 THEN 25 
            WHEN id_petugas_lab = 118 THEN 27 
            WHEN id_petugas_lab = 120 THEN 28
            WHEN id_petugas_lab = 121 THEN 29
            WHEN id_petugas_lab = 122 THEN 30 
            WHEN id_petugas_lab = 123 THEN 31  
            WHEN id_petugas_lab = 124 THEN 32 
            WHEN id_petugas_lab = 125 THEN 33 
            WHEN id_petugas_lab = 126 THEN 34
            WHEN id_petugas_lab = 127 THEN 35
            WHEN id_petugas_lab = 128 THEN 36 
            WHEN id_petugas_lab = 129 THEN 37  
            WHEN id_petugas_lab = 130 THEN 38 
            WHEN id_petugas_lab = 131 THEN 39 
            WHEN id_petugas_lab = 132 THEN 40
            WHEN id_petugas_lab = 133 THEN 41
            WHEN id_petugas_lab = 135 THEN 44 
            WHEN id_petugas_lab = 138 THEN 45  
            WHEN id_petugas_lab = 139 THEN 42
            ELSE id_petugas_lab = 42
        END;
    """)

    cursor.execute("""
                
                UPDATE transaksi_lab_detail
                JOIN transaksi_lab ON transaksi_lab_detail.id_transaksi_lab = transaksi_lab.id_transaksi_lab
                SET transaksi_lab_detail.user_validasi = transaksi_lab.id_petugas_lab;
                
                """)
    

    conn.commit()
    print("✅ Semua update berhasil dijalankan.")
except Exception as e:
    print(f"❌ Error saat update: {e}")
    conn.rollback()

cursor.close()
conn.close()
