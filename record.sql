-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 02, 2019 at 10:43 AM
-- Server version: 10.1.33-MariaDB
-- PHP Version: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `record`
--

-- --------------------------------------------------------

--
-- Table structure for table `detail`
--

CREATE TABLE `detail` (
  `S.No` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `District` varchar(50) NOT NULL,
  `Contact_No` int(20) NOT NULL,
  `Email_id` varchar(50) NOT NULL,
  `course` varchar(50) NOT NULL,
  `question` varchar(100) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `detail`
--

INSERT INTO `detail` (`S.No`, `Name`, `Gender`, `Address`, `District`, `Contact_No`, `Email_id`, `course`, `question`, `Date`) VALUES
(12, 'mukund', 'male', 'basopatti', 'madhubani', 56234, 'bksxnkjsxn', 'python', 'hvhvuwgvdu', '2019-07-23'),
(13, 'murarka', 'male', 'basopatti', 'madhubani', 5644545, 'bksxnkjsxn', 'c++', 'hvhvuwgvdu', '2019-07-23'),
(14, 'krishna', 'male', 'madhepur', 'madhubani', 55522, 'bksxnkjn', 'java', 'hvhvuwgvdu', '2019-07-23'),
(15, 'umashanker', 'male', 'aara', 'dbg', 23654, 'bhbahbuh', 'c#', 'hvhvuwgvdu', '2019-07-23'),
(16, 'sonu', 'male', 'chapra', 'dbg', 895623, 'nsjni', 'android', 'hvhvuwgvdu', '2019-07-23'),
(17, 'puja', 'female', 'jaso', 'madhubani', 456789, 'nijnijiq', 'python', 'sqkijk', '2019-07-25'),
(18, 'puja', 'female', 'arghawa', 'madhubani', 2147483647, 'nijnijiq', 'python', 'sqkijk', '2019-07-25'),
(19, 'arti', 'female', 'radh', 'dbg', 2147483647, 'nijnijiq', 'java', 'sqkijk', '2019-07-25'),
(20, 'anu', 'female', 'kalna', 'mfp', 2147483647, 'nijnijiq', 'android', 'sqkijk', '2019-07-25'),
(21, 'sunita', 'female', 'pupri', 'srs', 2147483647, 'nijnijiq', 'c#', 'sqkijk', '2019-07-25'),
(22, 'sneha', 'female', 'chowki', 'pnbe', 2147483647, 'nijnijiq', 'python', 'sqkijk', '2019-07-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detail`
--
ALTER TABLE `detail`
  ADD PRIMARY KEY (`S.No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `detail`
--
ALTER TABLE `detail`
  MODIFY `S.No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
