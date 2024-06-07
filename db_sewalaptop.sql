-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 03 Jun 2024 pada 09.00
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_test`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `list_laptop`
--

CREATE TABLE `list_laptop` (
  `kode_laptop` varchar(50) NOT NULL,
  `harga_sewa` varchar(50) NOT NULL,
  `status` varchar(10) DEFAULT NULL,
  `jenis_laptop` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `list_laptop`
--

INSERT INTO `list_laptop` (`kode_laptop`, `harga_sewa`, `status`, `jenis_laptop`) VALUES
('A01', '3000', NULL, 'GTX 1080'),
('A02', '6000', NULL, 'RTX 2080'),
('A03', '5000', NULL, 'GTX 1090'),
('A04', '10000', NULL, 'Lenovo Legion S23 Ultra Pro'),
('A05', '5000', NULL, 'RTX 9090');

-- --------------------------------------------------------

--
-- Struktur dari tabel `sewa_laptop`
--

CREATE TABLE `sewa_laptop` (
  `id_sewa` int(11) NOT NULL,
  `kode_laptop` varchar(20) NOT NULL,
  `jenis_laptop` varchar(30) NOT NULL,
  `harga_sewa` varchar(30) NOT NULL,
  `total_harga` varchar(30) DEFAULT NULL,
  `jam_mulai` time NOT NULL,
  `jam_akhir` time DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `sewa_laptop`
--

INSERT INTO `sewa_laptop` (`id_sewa`, `kode_laptop`, `jenis_laptop`, `harga_sewa`, `total_harga`, `jam_mulai`, `jam_akhir`, `created_at`) VALUES
(1, 'A01', 'GTX 1080', '3000.0', '3000.0', '18:13:01', '18:13:03', '2024-05-28 18:13:01'),
(2, 'A03', 'GTX 1090', '5000.0', '5000.0', '18:16:02', '18:16:06', '2024-05-28 18:16:02'),
(3, 'A02', 'RTX 2080', '6000.0', '6000.0', '18:18:49', '18:18:52', '2024-05-28 18:18:49'),
(4, 'A02', 'RTX 2080', '6000.0', '6000.0', '18:20:19', '18:20:22', '2024-05-28 18:20:19'),
(5, 'A04', 'Lenovo Legion S23 Ultra Pro', '10000.0', '10000.0', '18:21:01', '18:21:04', '2024-05-28 18:21:01'),
(6, 'A01', 'GTX 1080', '3000.0', '3000.0', '18:22:01', '18:22:03', '2024-05-28 18:22:01'),
(7, 'A03', 'GTX 1090', '5000.0', '5000.0', '18:22:19', '18:22:22', '2024-05-28 18:22:19'),
(8, 'A02', 'RTX 2080', '6000.0', '6000.0', '18:23:18', '18:23:20', '2024-05-28 18:23:18'),
(9, 'A03', 'GTX 1090', '5000.0', '5000.0', '18:23:47', '18:24:01', '2024-05-28 18:23:47'),
(10, 'A05', 'RTX 9090', '5000.0', '5000.0', '18:23:57', '18:33:26', '2024-05-28 18:23:57'),
(11, 'A03', 'GTX 1090', '5000.0', '5000.0', '18:33:14', '18:33:17', '2024-05-28 18:33:14'),
(12, 'A03', 'GTX 1090', '5000.0', '5000.0', '18:38:44', '18:38:47', '2024-05-28 18:38:44'),
(13, 'A03', 'GTX 1090', '5000.0', '5000.0', '18:42:34', '18:42:37', '2024-05-28 18:42:34'),
(14, 'A02', 'RTX 2080', '6000.0', '6000.0', '18:57:34', '18:57:36', '2024-05-28 18:57:34'),
(15, 'A01', 'GTX 1080', '3000.0', '3000.0', '19:07:39', '19:07:42', '2024-05-28 19:07:39'),
(16, 'A02', 'RTX 2080', '6000.0', '6000.0', '19:12:51', '19:12:54', '2024-05-28 19:12:51'),
(17, 'A02', 'RTX 2080', '6000.0', '6000.0', '08:09:15', '08:09:22', '2024-05-29 08:09:15'),
(18, 'A01', 'GTX 1080', '3000.0', '3000.0', '21:42:08', '21:42:24', '2024-06-02 21:42:08');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `tipe_akun` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`username`, `password`, `nama`, `tipe_akun`) VALUES
('', '', NULL, ''),
('faris', '123', 'Faris', 'admin'),
('Tes', '123', NULL, ''),
('user', '123', 'User', '');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `list_laptop`
--
ALTER TABLE `list_laptop`
  ADD PRIMARY KEY (`kode_laptop`);

--
-- Indeks untuk tabel `sewa_laptop`
--
ALTER TABLE `sewa_laptop`
  ADD PRIMARY KEY (`id_sewa`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `sewa_laptop`
--
ALTER TABLE `sewa_laptop`
  MODIFY `id_sewa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
