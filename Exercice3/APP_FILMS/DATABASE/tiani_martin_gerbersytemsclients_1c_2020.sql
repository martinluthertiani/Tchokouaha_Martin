--

-- Database: TIANI_MARTIN_GERBERSYSTEMSCLIENTS_1C_2020

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE if exists TIANI_MARTIN_GERBERSYSTEMSCLIENTS_1C_2020;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS TIANI_MARTIN_GERBERSYSTEMSCLIENTS_1C_2020;

-- Utilisation de cette base de donnée

USE TIANI_MARTIN_GERBERSYSTEMSCLIENTS_1C_2020; 

-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mer 20 Mai 2020 à 05:28
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `tiani_martin_gerbersytemsclients_1c_2020`
--

-- --------------------------------------------------------

--
-- Structure de la table `t_abonnements`
--

CREATE TABLE `t_abonnements` (
  `id_Abo` int(11) NOT NULL,
  `Nom_Abo` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_abonnements`
--

INSERT INTO `t_abonnements` (`id_Abo`, `Nom_Abo`) VALUES
(1, 'Kaspersky'),
(2, 'Business Central'),
(3, 'Office 365'),
(4, 'Salary 365'),
(5, 'WinBiz'),
(6, 'Carbonite');

-- --------------------------------------------------------

--
-- Structure de la table `t_adresses`
--

CREATE TABLE `t_adresses` (
  `id_Adresse` int(11) NOT NULL,
  `Nom_Adresse` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_adresses`
--

INSERT INTO `t_adresses` (`id_Adresse`, `Nom_Adresse`) VALUES
(1, 'Rue de la Plaine 67, 1400 Yverdon-les-Bains'),
(2, 'Rue d\'Orbe 63, 1400 Yverdon-les-Bains'),
(3, 'Avenue des Boveresses 52, 1000 Lausanne'),
(4, 'Rue de Genève 63, 1002 Lausanne'),
(5, 'Chemin de Dévent 7, 1024 Ecublens'),
(6, 'Route de Lausanne 6, 1040 Echallens');

-- --------------------------------------------------------

--
-- Structure de la table `t_comptes`
--

CREATE TABLE `t_comptes` (
  `id_Compte` int(11) NOT NULL,
  `IBAN` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_comptes`
--

INSERT INTO `t_comptes` (`id_Compte`, `IBAN`) VALUES
(1, 'CH2500051268547684'),
(2, 'CH282356000E53246987'),
(3, 'CH1172466449976254'),
(4, 'CH402356000023489'),
(5, 'CH1887960000Z2153'),
(6, 'CH4500024584T1247');

-- --------------------------------------------------------

--
-- Structure de la table `t_contrats`
--

CREATE TABLE `t_contrats` (
  `id_Contrat` int(11) NOT NULL,
  `Type_Contrat` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_contrats`
--

INSERT INTO `t_contrats` (`id_Contrat`, `Type_Contrat`) VALUES
(1, 'Tacite'),
(2, 'Hebergement'),
(3, 'Conseil'),
(4, 'Maintenance'),
(5, 'Vente');

-- --------------------------------------------------------

--
-- Structure de la table `t_logiciels`
--

CREATE TABLE `t_logiciels` (
  `id_Logiciel` int(11) NOT NULL,
  `Nom_Logiciel` varchar(60) NOT NULL,
  `Cle_Logiciel` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_logiciels`
--

INSERT INTO `t_logiciels` (`id_Logiciel`, `Nom_Logiciel`, `Cle_Logiciel`) VALUES
(1, 'Windows 10 ', 'DFRE-1254-G758-2588'),
(2, 'Windows Servers 2012 R2', 'E45H-MNJU-4578_9874'),
(3, 'Photoshop Pro', '9455-D7895-2547-FGFR'),
(4, 'Visio Pro', 'DU54-2587-M325-MMN1'),
(5, 'Windows Servers 2019', 'OIZG-1254-7894-L3658'),
(6, 'Suite Office entreprise 2019', 'EERW-4578-D258-8979');

-- --------------------------------------------------------

--
-- Structure de la table `t_mails`
--

CREATE TABLE `t_mails` (
  `id_Mails` int(11) NOT NULL,
  `Nom_Mail` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_mails`
--

INSERT INTO `t_mails` (`id_Mails`, `Nom_Mail`) VALUES
(1, 'martinluther.tiani@bluewin.ch'),
(2, 'merlinroky@gmail.com'),
(3, 'laila.grivet@yahoo.fr'),
(4, 'prisca.demierre@hotmail.com'),
(6, 'eric.zassi@yahoo.fr'),
(8, 'je vous aime '),
(9, 'je vous aime '),
(10, 'je vous aime ');

-- --------------------------------------------------------

--
-- Structure de la table `t_materiels`
--

CREATE TABLE `t_materiels` (
  `id_Materiel` int(11) NOT NULL,
  `Nom_Materiel` varchar(60) NOT NULL,
  `NumSerie_Materiel` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_materiels`
--

INSERT INTO `t_materiels` (`id_Materiel`, `Nom_Materiel`, `NumSerie_Materiel`) VALUES
(1, 'ASA 5505', 'SN99898995858'),
(2, 'Lenovo ThinkCentre M720q', 'SN9474179825555'),
(3, 'Surface Pro 5', 'SN74566625929322'),
(4, 'Ipad pro 2019', 'SN754552596252666'),
(5, 'Samsung G254', 'SN174595665665'),
(6, 'Moniteur Lenovo ThinkVision T24i', 'SN62686855885859');

-- --------------------------------------------------------

--
-- Structure de la table `t_personnes`
--

CREATE TABLE `t_personnes` (
  `id_Pers` int(11) NOT NULL,
  `Nom_Pers` varchar(50) NOT NULL,
  `Prenom_Pers` varchar(40) NOT NULL,
  `RaisonSociale_Pers` varchar(60) NOT NULL,
  `NomRespo_Pers` varchar(50) NOT NULL,
  `PrenomRespo_Pers` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_personnes`
--

INSERT INTO `t_personnes` (`id_Pers`, `Nom_Pers`, `Prenom_Pers`, `RaisonSociale_Pers`, `NomRespo_Pers`, `PrenomRespo_Pers`) VALUES
(1, 'Lauby', 'Henri', '', '', ''),
(2, 'EMS Les Châteaux', '', 'Fondation Les Châteaux', 'Meunier', 'Albert'),
(3, 'Tiani', 'Luther', '', '', ''),
(4, 'AVDEMS', '', 'AVDEMS', 'Morandini', 'Lionel'),
(5, 'Garage Carlos', '', 'Garage Carlos SA', 'Grivet', 'Pascal'),
(6, 'Fiduciaire Monet', '', 'Fiduciaire Monet SA', 'Monet', 'Charles'),
(7, 'Zassi', 'Martin Luther', 'Zassi SA', 'Tchokouaha', 'François'),
(8, '', '', '', '', '');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_abos`
--

CREATE TABLE `t_pers_abos` (
  `id_Pers_Abo` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Abo` int(11) NOT NULL,
  `DateDebut_Abo` date NOT NULL,
  `DateFin_Abo` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_abos`
--

INSERT INTO `t_pers_abos` (`id_Pers_Abo`, `fk_Pers`, `fk_Abo`, `DateDebut_Abo`, `DateFin_Abo`) VALUES
(1, 2, 3, '2020-03-03', '2025-03-02'),
(2, 3, 4, '2020-02-05', '2022-02-04'),
(3, 1, 5, '2020-01-21', '2023-01-20');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_adresses`
--

CREATE TABLE `t_pers_adresses` (
  `id_Pers_Adresse` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Adresse` int(11) NOT NULL,
  `DateEnreg_Adresse` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_adresses`
--

INSERT INTO `t_pers_adresses` (`id_Pers_Adresse`, `fk_Pers`, `fk_Adresse`, `DateEnreg_Adresse`) VALUES
(1, 6, 2, '2020-03-04'),
(2, 5, 3, '2020-03-04'),
(3, 2, 1, '2020-02-12');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_comptes`
--

CREATE TABLE `t_pers_comptes` (
  `id_Pers_Compte` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Compte` int(11) NOT NULL,
  `DateEnreg_Compte` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_comptes`
--

INSERT INTO `t_pers_comptes` (`id_Pers_Compte`, `fk_Pers`, `fk_Compte`, `DateEnreg_Compte`) VALUES
(1, 4, 5, '2020-03-04'),
(2, 3, 2, '2020-03-03'),
(3, 1, 6, '2019-12-11');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_contrats`
--

CREATE TABLE `t_pers_contrats` (
  `id_Pers_Contrat` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Contrat` int(11) NOT NULL,
  `DateDebut_Contrat` date NOT NULL,
  `DateFin_Contrat` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_contrats`
--

INSERT INTO `t_pers_contrats` (`id_Pers_Contrat`, `fk_Pers`, `fk_Contrat`, `DateDebut_Contrat`, `DateFin_Contrat`) VALUES
(1, 2, 4, '2020-03-02', '2024-03-01'),
(2, 1, 3, '2020-02-05', '2022-02-04'),
(3, 4, 1, '2020-01-15', '2025-01-14');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_logiciels`
--

CREATE TABLE `t_pers_logiciels` (
  `id_Pers_Logiciel` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Logiciel` int(11) NOT NULL,
  `DateAchat_Logiciel` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_logiciels`
--

INSERT INTO `t_pers_logiciels` (`id_Pers_Logiciel`, `fk_Pers`, `fk_Logiciel`, `DateAchat_Logiciel`) VALUES
(3, 1, 6, '2020-03-04'),
(4, 3, 4, '2020-02-09'),
(5, 5, 2, '2020-02-04');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_mails`
--

CREATE TABLE `t_pers_mails` (
  `id_Pers_Mail` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Mails` int(11) NOT NULL,
  `DateEnreg_Mail` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_mails`
--

INSERT INTO `t_pers_mails` (`id_Pers_Mail`, `fk_Pers`, `fk_Mails`, `DateEnreg_Mail`) VALUES
(1, 5, 2, '2019-12-12'),
(2, 3, 1, '2020-02-25'),
(3, 1, 4, '2020-03-08'),
(4, 1, 3, '2020-04-30');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_materiels`
--

CREATE TABLE `t_pers_materiels` (
  `id_Pers_Materiel` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Materiel` int(11) NOT NULL,
  `DateAchat_Materiel` date NOT NULL,
  `DateFinGarantie_Materiel` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_materiels`
--

INSERT INTO `t_pers_materiels` (`id_Pers_Materiel`, `fk_Pers`, `fk_Materiel`, `DateAchat_Materiel`, `DateFinGarantie_Materiel`) VALUES
(1, 1, 5, '2020-03-10', '2021-03-09'),
(2, 3, 6, '2020-03-06', '2023-03-05'),
(3, 4, 2, '2020-02-04', '2022-02-03');

-- --------------------------------------------------------

--
-- Structure de la table `t_pers_teleph`
--

CREATE TABLE `t_pers_teleph` (
  `id_Pers_Teleph` int(11) NOT NULL,
  `fk_Pers` int(11) NOT NULL,
  `fk_Teleph` int(11) NOT NULL,
  `DateEnreg_Teleph` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_pers_teleph`
--

INSERT INTO `t_pers_teleph` (`id_Pers_Teleph`, `fk_Pers`, `fk_Teleph`, `DateEnreg_Teleph`) VALUES
(1, 6, 1, '2020-03-07'),
(2, 1, 4, '2020-02-12'),
(3, 3, 5, '2020-03-02'),
(4, 7, 3, '2020-04-03'),
(5, 8, 4, '2020-04-03'),
(6, 8, 4, '2020-03-03'),
(7, 8, 4, '2020-04-03'),
(8, 2, 2, '2020-04-03'),
(9, 2, 4, '2020-04-03'),
(10, 6, 3, '2020-04-03'),
(11, 1, 3, '2020-04-03'),
(12, 1, 3, '2020-04-03'),
(13, 1, 3, '2020-04-30'),
(14, 1, 3, '2020-04-30'),
(15, 1, 3, '2020-04-30');

-- --------------------------------------------------------

--
-- Structure de la table `t_telephones`
--

CREATE TABLE `t_telephones` (
  `id_Teleph` int(11) NOT NULL,
  `Num_Teleph` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_telephones`
--

INSERT INTO `t_telephones` (`id_Teleph`, `Num_Teleph`) VALUES
(1, '0788325352'),
(2, '0798340582'),
(3, '0765258798'),
(4, '0772556988'),
(5, '0246441010'),
(6, '0216856363');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_abonnements`
--
ALTER TABLE `t_abonnements`
  ADD PRIMARY KEY (`id_Abo`);

--
-- Index pour la table `t_adresses`
--
ALTER TABLE `t_adresses`
  ADD PRIMARY KEY (`id_Adresse`);

--
-- Index pour la table `t_comptes`
--
ALTER TABLE `t_comptes`
  ADD PRIMARY KEY (`id_Compte`);

--
-- Index pour la table `t_contrats`
--
ALTER TABLE `t_contrats`
  ADD PRIMARY KEY (`id_Contrat`);

--
-- Index pour la table `t_logiciels`
--
ALTER TABLE `t_logiciels`
  ADD PRIMARY KEY (`id_Logiciel`);

--
-- Index pour la table `t_mails`
--
ALTER TABLE `t_mails`
  ADD PRIMARY KEY (`id_Mails`);

--
-- Index pour la table `t_materiels`
--
ALTER TABLE `t_materiels`
  ADD PRIMARY KEY (`id_Materiel`);

--
-- Index pour la table `t_personnes`
--
ALTER TABLE `t_personnes`
  ADD PRIMARY KEY (`id_Pers`);

--
-- Index pour la table `t_pers_abos`
--
ALTER TABLE `t_pers_abos`
  ADD PRIMARY KEY (`id_Pers_Abo`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Abo` (`fk_Abo`);

--
-- Index pour la table `t_pers_adresses`
--
ALTER TABLE `t_pers_adresses`
  ADD PRIMARY KEY (`id_Pers_Adresse`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Adresse` (`fk_Adresse`);

--
-- Index pour la table `t_pers_comptes`
--
ALTER TABLE `t_pers_comptes`
  ADD PRIMARY KEY (`id_Pers_Compte`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Compte` (`fk_Compte`);

--
-- Index pour la table `t_pers_contrats`
--
ALTER TABLE `t_pers_contrats`
  ADD PRIMARY KEY (`id_Pers_Contrat`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Contrat` (`fk_Contrat`);

--
-- Index pour la table `t_pers_logiciels`
--
ALTER TABLE `t_pers_logiciels`
  ADD PRIMARY KEY (`id_Pers_Logiciel`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Logiciel` (`fk_Logiciel`);

--
-- Index pour la table `t_pers_mails`
--
ALTER TABLE `t_pers_mails`
  ADD PRIMARY KEY (`id_Pers_Mail`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Mail` (`fk_Mails`);

--
-- Index pour la table `t_pers_materiels`
--
ALTER TABLE `t_pers_materiels`
  ADD PRIMARY KEY (`id_Pers_Materiel`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Materiel` (`fk_Materiel`);

--
-- Index pour la table `t_pers_teleph`
--
ALTER TABLE `t_pers_teleph`
  ADD PRIMARY KEY (`id_Pers_Teleph`),
  ADD KEY `fk_Pers` (`fk_Pers`),
  ADD KEY `fk_Teleph` (`fk_Teleph`);

--
-- Index pour la table `t_telephones`
--
ALTER TABLE `t_telephones`
  ADD PRIMARY KEY (`id_Teleph`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_abonnements`
--
ALTER TABLE `t_abonnements`
  MODIFY `id_Abo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_adresses`
--
ALTER TABLE `t_adresses`
  MODIFY `id_Adresse` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_comptes`
--
ALTER TABLE `t_comptes`
  MODIFY `id_Compte` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_contrats`
--
ALTER TABLE `t_contrats`
  MODIFY `id_Contrat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT pour la table `t_logiciels`
--
ALTER TABLE `t_logiciels`
  MODIFY `id_Logiciel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_mails`
--
ALTER TABLE `t_mails`
  MODIFY `id_Mails` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT pour la table `t_materiels`
--
ALTER TABLE `t_materiels`
  MODIFY `id_Materiel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_personnes`
--
ALTER TABLE `t_personnes`
  MODIFY `id_Pers` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT pour la table `t_pers_abos`
--
ALTER TABLE `t_pers_abos`
  MODIFY `id_Pers_Abo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_pers_adresses`
--
ALTER TABLE `t_pers_adresses`
  MODIFY `id_Pers_Adresse` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_pers_comptes`
--
ALTER TABLE `t_pers_comptes`
  MODIFY `id_Pers_Compte` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_pers_contrats`
--
ALTER TABLE `t_pers_contrats`
  MODIFY `id_Pers_Contrat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_pers_logiciels`
--
ALTER TABLE `t_pers_logiciels`
  MODIFY `id_Pers_Logiciel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT pour la table `t_pers_mails`
--
ALTER TABLE `t_pers_mails`
  MODIFY `id_Pers_Mail` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `t_pers_materiels`
--
ALTER TABLE `t_pers_materiels`
  MODIFY `id_Pers_Materiel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_pers_teleph`
--
ALTER TABLE `t_pers_teleph`
  MODIFY `id_Pers_Teleph` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT pour la table `t_telephones`
--
ALTER TABLE `t_telephones`
  MODIFY `id_Teleph` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_pers_abos`
--
ALTER TABLE `t_pers_abos`
  ADD CONSTRAINT `t_pers_abos_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_abos_ibfk_2` FOREIGN KEY (`fk_Abo`) REFERENCES `t_abonnements` (`id_Abo`);

--
-- Contraintes pour la table `t_pers_adresses`
--
ALTER TABLE `t_pers_adresses`
  ADD CONSTRAINT `t_pers_adresses_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_adresses_ibfk_2` FOREIGN KEY (`fk_Adresse`) REFERENCES `t_adresses` (`id_Adresse`);

--
-- Contraintes pour la table `t_pers_comptes`
--
ALTER TABLE `t_pers_comptes`
  ADD CONSTRAINT `t_pers_comptes_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_comptes_ibfk_2` FOREIGN KEY (`fk_Compte`) REFERENCES `t_comptes` (`id_Compte`);

--
-- Contraintes pour la table `t_pers_contrats`
--
ALTER TABLE `t_pers_contrats`
  ADD CONSTRAINT `t_pers_contrats_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_contrats_ibfk_2` FOREIGN KEY (`fk_Contrat`) REFERENCES `t_contrats` (`id_Contrat`);

--
-- Contraintes pour la table `t_pers_logiciels`
--
ALTER TABLE `t_pers_logiciels`
  ADD CONSTRAINT `t_pers_logiciels_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_logiciels_ibfk_2` FOREIGN KEY (`fk_Logiciel`) REFERENCES `t_logiciels` (`id_Logiciel`);

--
-- Contraintes pour la table `t_pers_mails`
--
ALTER TABLE `t_pers_mails`
  ADD CONSTRAINT `t_pers_mails_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_mails_ibfk_2` FOREIGN KEY (`fk_Mails`) REFERENCES `t_mails` (`id_Mails`);

--
-- Contraintes pour la table `t_pers_materiels`
--
ALTER TABLE `t_pers_materiels`
  ADD CONSTRAINT `t_pers_materiels_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_materiels_ibfk_2` FOREIGN KEY (`fk_Materiel`) REFERENCES `t_materiels` (`id_Materiel`);

--
-- Contraintes pour la table `t_pers_teleph`
--
ALTER TABLE `t_pers_teleph`
  ADD CONSTRAINT `t_pers_teleph_ibfk_1` FOREIGN KEY (`fk_Pers`) REFERENCES `t_personnes` (`id_Pers`),
  ADD CONSTRAINT `t_pers_teleph_ibfk_2` FOREIGN KEY (`fk_Teleph`) REFERENCES `t_telephones` (`id_Teleph`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
