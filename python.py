# Skrip Python untuk menggantikan variabel
with open('README.md', 'r') as file:
    content = file.read()

# Gantikan variabel dengan nilai yang diinginkan
content = content.replace('${{ github.repository_owner }}', 'NamaPengguna')

# Simpan hasil kembali ke file
with open('README.md', 'w') as file:
    file.write(content)
