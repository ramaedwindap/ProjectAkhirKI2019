# menggunakan wave package untuk ekstraksi audio file
import wave
song = wave.open("song_embedded.wav", mode='rb')
# konversi audio menjadi biner
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# ekstraksi lsb pada tiap byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# konversi biner ke teks
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# melakukan perubahan karakter
decoded = string.split("###")[0]

# menampilkan hasil
print("Data berhasil di Ekstraksi: "+decoded)
song.close()