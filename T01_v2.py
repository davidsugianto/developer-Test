import re

a = raw_input("masukkan No handphone <spasi> nama lengkap <spasi> usia <spasi> email : ")

email = re.search(r'\w+@[\w.]+', a)
nohp = re.search(r'(\d{3}[-\.\s]??\d{5}[-\.\s]??\d{5}|\(\d{3}\)\s*\d{5}[-\.\s]??\d{10}|\d{3}[-\.\s]??\d{10})',a)
nama = re.search(r'([A-Za-z\s]+)', a)
usia = re.search(r'(?:^|\s)(\d{2})(?:\s|$)',a)

print "Nomor Handphone :  "+ nohp.group()
print "Nama 	       	: "+ nama.group()
print "Usia 	       	: "+ usia.group() +"Tahun"
print "E-mail 	       	:  "+ email.group()
