#L0123064 Hellen Aurelia Syafaatunnas
#L0123071 Josephine Angelia Pramudya
#L0123072 Kamila Rosyidah

import numpy as np

# Menyusun Solusi Persamaan Linear

def solve_linear_equation():
    print("Masukkan jumlah baris untuk matriks A:")
    rows_A = int(input())
    print("Masukkan jumlah kolom untuk matriks A:")
    cols_A = int(input())

    # Input Matrix
    print("Masukkan koefisien matriks A:")
    a = np.array([list(map(float, input().split())) for _ in range(rows_A)])
    print("Masukkan jumlah baris untuk matriks B (harus sama dengan jumlah kolom di matriks A):")
    rows_B = int(input())

    if rows_B != rows_A:
        print("Error: Jumlah baris di matriks B harus sama dengan jumlah baris di matriks A.")
        return

    print("Masukkan koefisien matriks B:")
    b = np.array([list(map(float, input().split())) for _ in range(rows_B)])

    # Pemilihan Metode Penyelesaian
    print("\nPilih metode untuk menyelesaikan sistem persamaan linear:")
    print("1. Eliminasi Gauss-Jordan")
    print("2. Eliminasi Gauss")
    print("3. Invers Matriks")
    method_choice = int(input("Masukkan pilihan Anda: "))

    if method_choice == 1:
        try:
            x = np.linalg.solve(a, b)
            print("Solusi dari sistem persamaan linear adalah:")
            print(x)
        except np.linalg.LinAlgError:
            print("\nError: Sistem persamaan linear tidak memiliki solusi unik atau singular.")
    elif method_choice == 2:
        # Implementasi metode Eliminasi Gauss
        x = gauss_elimination(a, b)
        if x is None:
            print("\nMaaf, tidak ditemukan solusi dengan metode Eliminasi Gauss.")
        else:
            print("Solusi dari sistem persamaan linear adalah:")
            print(x)
    elif method_choice == 3:
        try:
            a_inv = np.linalg.inv(a)
            x = np.dot(a_inv, b)
            print("Solusi dari sistem persamaan linear adalah:")
            print(x)
        except np.linalg.LinAlgError:
            print("\nError: Sistem persamaan linear tidak memiliki solusi unik atau singular.")
    else:
        print("Pilihan metode tidak valid.")

#Mencari Inverse
def find_inverse():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    a_inv = np.linalg.inv(a)
    print("Invers matriks A adalah:")
    print(a_inv)

def gauss_elimination(a, b):
    # Implementasi metode Eliminasi Gauss
    # Jika tidak ditemukan solusi, kembalikan None
    # Jika ditemukan solusi, kembalikan solusi tersebut
    pass

# Mencari Karakteristik Polinomial
def find_polynomial_characteristic():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    charpoly = np.poly(a)
    print("\nKarakteristik Polinomial dari A adalah:")
    print(charpoly)

# Mencari Determinan
def find_determinant():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    det = np.linalg.det(a)
    print("\nDeterminan dari A adalah:")
    print(det)
    
# Mencari Nilai Eigen dan Vektor Eigen
def find_eigen():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    eigvals, eigvecs = np.linalg.eig(a)
    print("\nNilai eigen dari A adalah:")
    print(eigvals)
    print("\nVektor eigen dari A adalah:")
    for vec in eigvecs:
        print(vec[:3])  

# Mencari Dekomposisi Nilai Tunggal (SVD)
def find_svd():
    print("Masukkan matriks:")
    a = np.array([input().split() for _ in range(n)], dtype=float)
    u, s, vh = np.linalg.svd(a)
    print("\nHasil SVD dari matriks A:")
    print("U:")
    print(u)
    print("Nilai Singular:")
    print(s)
    print("Vh (Transpose dari V):")
    print(vh)

# Menambahkan Fungsi untuk SPL Kompleks dengan Gauss
def spl_complex():
    n = int(input("Masukkan jumlah baris: "))
    m = int(input("Masukkan jumlah kolom: "))
    print(f"Masukkan koefisien matriks A (ukuran {n}x{m}):")
    A = []
    for _ in range(n):
        row = [np.complex_(x) for x in input().split()]
        A.append(row)
    A = np.array(A)
    matrix1 = str(A)
    print(f"Masukkan vektor b (dengan ukuran {n} tulis secara mendatar):")
    B = np.array([np.complex_(x) for x in input().split()])
    matrix2 = str(B)

    def splgaus(A, b):
        n = len(b)
        # Fase Eliminasi
        for k in range(0, n-1):
            for i in range(k+1, n):
                if A[i, k] != 0.0:
                    lam = A[i, k] / A[k, k]
                    A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                    b[i] = b[i] - lam * b[k]

        # Substitusi Mundur
        x = np.zeros_like(b, dtype=complex)
        for k in range(n-1, -1, -1):
            x[k] = (b[k] - np.dot(A[k, k+1:n], x[k+1:n])) / A[k, k]
        return x

    solution = splgaus(A, B)

    augmented_matrix = np.hstack((A, B.reshape(-1, 1)))
    temp_matrix = np.linalg.matrix_rank(augmented_matrix)
    cols = A.shape[1]

    if solution is None:
        print("Tidak ada Solusi")
    elif temp_matrix < cols:
        print("Solusi Tak Terbatas")
    else:
        print("Solusi Unik:")
        for i in range(n):
            print(f"x{i+1} = {np.round(solution[i])}")

# Membuat Tampilan Awal dan Menu Program
print("=== Kalkulator Aljabar Linier ===")
n = int(input("Masukkan ukuran matriks : "))

while True:
    print("\nPilih Operasi:")
    print("1. Sistem Persamaan Linier")
    print("2. Sistem Persamaan Linier Kompleks dengan Eliminasi Gauss")
    print("3. Determinan")
    print("4. Matriks Invers")
    print("5. Persamaan Polinomial")
    print("6. Nilai Eigen dan Vektor Eigen")
    print("7. Dekomposisi Nilai Tunggal (SVD)")
    print("8. Keluar")
    choice = int(input("\nMasukkan Pilihan: "))

    if choice == 1:
        solve_linear_equation()
    elif choice == 2:
        spl_complex()
    elif choice == 3:
        find_determinant()
    elif choice == 4:
        find_inverse()
    elif choice == 5:
        find_polynomial_characteristic()
    elif choice == 6:
        find_eigen()
    elif choice == 7:
        find_svd()
    elif choice == 8:
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")