
import wave
# menginputkan audio
song = wave.open("song.wav", mode='rb')
# memaca frame dan merubah menjadi bit array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# isi pesan atau plaintext
string='KIFUNSIL'
string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
# konversi teks ke biner
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

# merubah tiap byte pada audio dengan satu bit pada bit teks array
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
# modifikasi byte
frame_modified = bytes(frame_bytes)

# membuat byte pada audio
with wave.open('song_embedded.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()