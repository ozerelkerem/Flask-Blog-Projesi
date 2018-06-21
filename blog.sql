-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 21 Haz 2018, 08:15:09
-- Sunucu sürümü: 10.1.26-MariaDB
-- PHP Sürümü: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `yb_blog`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `author` text NOT NULL,
  `content` text NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `articles`
--

INSERT INTO `articles` (`id`, `title`, `author`, `content`, `created_date`) VALUES
(2, 'Mustafa Kemal Atatürk\'ün Hayatı', 'deneme', '<p><img alt=\"\" src=\"http://i.milliyet.com.tr/YeniAnaResim/2017/11/09/fft99_mf10216965.Jpeg\" style=\"height:340px; width:606px\" /></p>\r\n\r\n<p><strong>Yaşasın Mustafa Kemal Atat&uuml;rk</strong></p>\r\n', '2018-06-21 00:59:45'),
(3, 'deneme makale', 'deneme', '<p>benim adım deneme</p>\r\n', '2018-06-21 01:41:51'),
(4, 'deneme kod pretty', 'deneme', '<pre class=\"prettyprint\">class Voila {\r\npublic:\r\n  // Voila\r\n  static const string VOILA = \"Voila\";\r\n\r\n  // will not interfere with embedded <a href=\"#voila2\">tags</a>.\r\n}</pre>', '2018-06-21 01:44:47');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`) VALUES
(1, 'Kerem Özerel', 'Kerem Özerel', 'Kerem Özerel', '$5$rounds=535000$mzexjiSpSlBwNHDp$QP/49CWcasS8fzfQQ2WBmryy53C.KQTe/Xtetbgz7S.'),
(2, 'ahmet', 'ahmet', 'ahmet', '$5$rounds=535000$3I6IFsjTNiBnRZVr$1aRgWlijHFQNARdBl3Caowa/7eXkd2O583LQMzLDJY9'),
(3, 'ahmet', 'ahmet', 'ahmet', '$5$rounds=535000$8GvoXMrYJ5a3wV6.$955f/mfXcwEEmYtIJUdxW1mc5oWuvYmbaibOUcQrsQ6'),
(4, 'ahmet', 'ahmet', 'ahmet', '$5$rounds=535000$.EdYAvitfeBCSAo5$r6BmS9HMhJkSP2ERoD2WCrndczq8PrXbDntPzP5BuK/'),
(5, 'sergen', 'sergen', 'sergen', '$5$rounds=535000$CYU7NmteSNpkAk5s$tBimH1xXyMNCXSD5a1iwB2tKDJKkAnpXtY3Mh2t8Oc8'),
(6, 'ahmet', 'ahmet', 'ahmet', '$5$rounds=535000$FHGiKhuO/M4npZKv$OqOF8a8c4ANMuk02vrub417YunfwTGGFhSFeOwpEtsB'),
(7, 'velii', 'veli@hotmail.com', 'velii', '$5$rounds=535000$9D0VI9iZdj5L1T.q$Hba03mKoB3uEGw5iXePwB/31LPePEWbMA5l8UfbxgrB'),
(8, 'deneme', 'deneme@hotmail.com', 'deneme', '$5$rounds=535000$Hh..OugRXTmpisVX$yB0Q/QLO1oUMf/5CGe9sK4qGKzIgilr/l3GFpU.JnDA');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
