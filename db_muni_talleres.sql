-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-12-2022 a las 22:34:40
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_muni_talleres`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add items taller', 7, 'add_itemstaller'),
(26, 'Can change items taller', 7, 'change_itemstaller'),
(27, 'Can delete items taller', 7, 'delete_itemstaller'),
(28, 'Can view items taller', 7, 'view_itemstaller'),
(29, 'Can add tipo taller', 8, 'add_tipotaller'),
(30, 'Can change tipo taller', 8, 'change_tipotaller'),
(31, 'Can delete tipo taller', 8, 'delete_tipotaller'),
(32, 'Can view tipo taller', 8, 'view_tipotaller'),
(33, 'Can add usuario', 9, 'add_usuario'),
(34, 'Can change usuario', 9, 'change_usuario'),
(35, 'Can delete usuario', 9, 'delete_usuario'),
(36, 'Can view usuario', 9, 'view_usuario'),
(37, 'Can add usuarioadmin', 10, 'add_usuarioadmin'),
(38, 'Can change usuarioadmin', 10, 'change_usuarioadmin'),
(39, 'Can delete usuarioadmin', 10, 'delete_usuarioadmin'),
(40, 'Can view usuarioadmin', 10, 'view_usuarioadmin'),
(41, 'Can add usuariofuncionario', 11, 'add_usuariofuncionario'),
(42, 'Can change usuariofuncionario', 11, 'change_usuariofuncionario'),
(43, 'Can delete usuariofuncionario', 11, 'delete_usuariofuncionario'),
(44, 'Can view usuariofuncionario', 11, 'view_usuariofuncionario'),
(45, 'Can add usuarioinstructor', 12, 'add_usuarioinstructor'),
(46, 'Can change usuarioinstructor', 12, 'change_usuarioinstructor'),
(47, 'Can delete usuarioinstructor', 12, 'delete_usuarioinstructor'),
(48, 'Can view usuarioinstructor', 12, 'view_usuarioinstructor'),
(49, 'Can add taller', 13, 'add_taller'),
(50, 'Can change taller', 13, 'change_taller'),
(51, 'Can delete taller', 13, 'delete_taller'),
(52, 'Can view taller', 13, 'view_taller'),
(53, 'Can add carro taller', 14, 'add_carrotaller'),
(54, 'Can change carro taller', 14, 'change_carrotaller'),
(55, 'Can delete carro taller', 14, 'delete_carrotaller'),
(56, 'Can view carro taller', 14, 'view_carrotaller'),
(57, 'Can add postulacion', 15, 'add_postulacion'),
(58, 'Can change postulacion', 15, 'change_postulacion'),
(59, 'Can delete postulacion', 15, 'delete_postulacion'),
(60, 'Can view postulacion', 15, 'view_postulacion'),
(61, 'Can add reporte', 16, 'add_reporte'),
(62, 'Can change reporte', 16, 'change_reporte'),
(63, 'Can delete reporte', 16, 'delete_reporte'),
(64, 'Can view reporte', 16, 'view_reporte'),
(65, 'Can add materiales', 17, 'add_materiales'),
(66, 'Can change materiales', 17, 'change_materiales'),
(67, 'Can delete materiales', 17, 'delete_materiales'),
(68, 'Can view materiales', 17, 'view_materiales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$VxzJAbq7nrf3UnatQhaMVa$p1GDJVOJaZvfxgr78tvYc6NGXz1EjcVUrC3qhxRRanE=', '2022-12-08 20:55:19.560866', 0, 'fernando', '', '', '', 0, 1, '2022-12-08 07:29:08.901928'),
(2, 'pbkdf2_sha256$320000$aqQ6Go963qPsaLO3CkQjNA$a6LFk1uLswBNfMVICGnVzgG6aqZTEe+J+rYkrgGn5Xo=', '2022-12-08 20:48:28.450185', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2022-12-08 15:44:44.241876');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_carrotaller`
--

CREATE TABLE `db_carrotaller` (
  `id` bigint(20) NOT NULL,
  `taller_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_items_taller`
--

CREATE TABLE `db_items_taller` (
  `id` bigint(20) NOT NULL,
  `codigoTaller` int(11) NOT NULL,
  `nombreTaller` varchar(40) NOT NULL,
  `descripcionTaller` varchar(300) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_items_taller`
--

INSERT INTO `db_items_taller` (`id`, `codigoTaller`, `nombreTaller`, `descripcionTaller`, `imagen`) VALUES
(1, 1, 'Manualidades', 'Taller entretenido para que puedas dibujar lo que te plazca o realizar manualidades en general (instructor Jaime Coloma horario 12:30 a 14:00)', 'talleres/index3_xMapjPJ.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_materiales`
--

CREATE TABLE `db_materiales` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_materiales`
--

INSERT INTO `db_materiales` (`codigo`, `nombre`, `descripcion`, `imagen`, `created_at`, `updated_at`) VALUES
(12, 'colchonetas', 'colchonetas para ejercicio', 'materiales/colchonetas_JYi9FtG.jpg', '2022-12-08', '2022-12-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_postulacion`
--

CREATE TABLE `db_postulacion` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_reporte`
--

CREATE TABLE `db_reporte` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_taller`
--

CREATE TABLE `db_taller` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `tipo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_taller`
--

INSERT INTO `db_taller` (`codigo`, `nombre`, `descripcion`, `imagen`, `created_at`, `updated_at`, `tipo_id`) VALUES
(1, 'Manualidades', 'Taller entretenido para que puedas dibujar lo que te plazca o realizar manualidades en general (instructor Jaime Coloma horario 12:30 a 14:00)', 'talleres/index3_xMapjPJ.jpg', '2022-12-08', '2022-12-08', 2),
(2, 'Ejercicio', 'Taller enfocado a realizar un poco de ejercicio con un especialista kinesiológico (instructor Adam Catril horario 14:30 a 16:00)', 'talleres/ejercicioadultomay_Gvohenx.jpg', '2022-12-08', '2022-12-08', 3),
(3, 'Baile', 'Taller dinámico para bailar cualquier tipo de música y que los recuerdos estén presentes (instructor Adam Catril horario 16:30 a 18:00)', 'talleres/tallerdebaile_1VsfPwo.jpg', '2022-12-08', '2022-12-08', 1),
(4, 'Canto', 'Taller dinámico para cantar con el ritmo de la música y que te llegue al corazón (instructor Orlando Echeverria horario 16:30 a 18:00)', 'talleres/tallerdemusica_DWWCmKx.jpg', '2022-12-08', '2022-12-08', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_tipo_taller`
--

CREATE TABLE `db_tipo_taller` (
  `id_tipo` int(11) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_tipo_taller`
--

INSERT INTO `db_tipo_taller` (`id_tipo`, `tipo`, `created_at`, `updated_at`) VALUES
(1, 'Baile', '2022-12-08', '2022-12-08'),
(2, 'Manualidades', '2022-12-08', '2022-12-08'),
(3, 'Ejercicio', '2022-12-08', '2022-12-08'),
(4, 'Canto', '2022-12-08', '2022-12-08'),
(5, 'Dibujo', '2022-12-08', '2022-12-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_usuario`
--

CREATE TABLE `db_usuario` (
  `run` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `comuna` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `direccion` varchar(80) NOT NULL,
  `correo` varchar(120) NOT NULL,
  `telefono` int(11) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_usuario`
--

INSERT INTO `db_usuario` (`run`, `nombre`, `apellido`, `comuna`, `region`, `direccion`, `correo`, `telefono`, `imagen`, `created_at`, `updated_at`) VALUES
(82928272, 'Fernando', 'Ibanez', 'la florida', 'Metropolitana', 'turquesa 18272', 'fer@gmail.com', 222927267, 'usuariosadulmayor/abuelomio_hSUaZM7.jpg', '2022-12-08', '2022-12-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_usuario_administrador`
--

CREATE TABLE `db_usuario_administrador` (
  `run` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `comuna` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `direccion` varchar(80) NOT NULL,
  `correo` varchar(120) NOT NULL,
  `telefono` int(11) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_usuario_administrador`
--

INSERT INTO `db_usuario_administrador` (`run`, `nombre`, `apellido`, `comuna`, `region`, `direccion`, `correo`, `telefono`, `imagen`, `created_at`, `updated_at`) VALUES
(167282722, 'Orlando', 'Echeverria', 'providencia', 'Metropolitana', 'pureza 28272', 'echeverria@gmail.com', 92827277, 'usuariosadmin/admistrador_wtxPiyR.jpg', '2022-12-08', '2022-12-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_usuario_funcionario`
--

CREATE TABLE `db_usuario_funcionario` (
  `run` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `comuna` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `direccion` varchar(80) NOT NULL,
  `correo` varchar(120) NOT NULL,
  `telefono` int(11) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_usuario_funcionario`
--

INSERT INTO `db_usuario_funcionario` (`run`, `nombre`, `apellido`, `comuna`, `region`, `direccion`, `correo`, `telefono`, `imagen`, `created_at`, `updated_at`) VALUES
(157367367, 'Diego', 'Kent', 'Puente alto', 'Metropolitana', 'los corraleros 2928', 'kent@gmail.com', 98272622, 'usuariosfuncionario/funcionario_S4gXcuL.jpg', '2022-12-08', '2022-12-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `db_usuario_instructor`
--

CREATE TABLE `db_usuario_instructor` (
  `run` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `comuna` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `direccion` varchar(80) NOT NULL,
  `correo` varchar(120) NOT NULL,
  `telefono` int(11) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `db_usuario_instructor`
--

INSERT INTO `db_usuario_instructor` (`run`, `nombre`, `apellido`, `comuna`, `region`, `direccion`, `correo`, `telefono`, `imagen`, `created_at`, `updated_at`) VALUES
(208272828, 'Adam', 'Catril', 'santa rosa', 'Metropolitana', 'jazmines 18272', 'adamc@gmail.com', 98272726, 'usuariosinstructor/insbaile_mOvdgkb.jpg', '2022-12-08', '2022-12-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-12-08 15:46:50.917146', '1', 'Baile', 1, '[{\"added\": {}}]', 8, 2),
(2, '2022-12-08 15:47:08.190386', '2', 'Manualidades', 1, '[{\"added\": {}}]', 8, 2),
(3, '2022-12-08 15:50:14.321125', '3', 'Ejercicio', 1, '[{\"added\": {}}]', 8, 2),
(4, '2022-12-08 15:50:19.699188', '4', 'Canto', 1, '[{\"added\": {}}]', 8, 2),
(5, '2022-12-08 15:50:57.793929', '5', 'Dibujo', 1, '[{\"added\": {}}]', 8, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(14, 'app', 'carrotaller'),
(7, 'app', 'itemstaller'),
(17, 'app', 'materiales'),
(15, 'app', 'postulacion'),
(16, 'app', 'reporte'),
(13, 'app', 'taller'),
(8, 'app', 'tipotaller'),
(9, 'app', 'usuario'),
(10, 'app', 'usuarioadmin'),
(11, 'app', 'usuariofuncionario'),
(12, 'app', 'usuarioinstructor'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-12-08 07:28:03.235010'),
(2, 'auth', '0001_initial', '2022-12-08 07:28:03.523656'),
(3, 'admin', '0001_initial', '2022-12-08 07:28:03.608754'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-12-08 07:28:03.618404'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-12-08 07:28:03.626985'),
(6, 'app', '0001_initial', '2022-12-08 07:28:03.760136'),
(7, 'app', '0002_postulacion_reporte', '2022-12-08 07:28:03.786952'),
(8, 'app', '0003_postulacion_imagen_reporte_imagen', '2022-12-08 07:28:03.807927'),
(9, 'contenttypes', '0002_remove_content_type_name', '2022-12-08 07:28:03.862967'),
(10, 'auth', '0002_alter_permission_name_max_length', '2022-12-08 07:28:03.902549'),
(11, 'auth', '0003_alter_user_email_max_length', '2022-12-08 07:28:03.917679'),
(12, 'auth', '0004_alter_user_username_opts', '2022-12-08 07:28:03.927228'),
(13, 'auth', '0005_alter_user_last_login_null', '2022-12-08 07:28:03.957410'),
(14, 'auth', '0006_require_contenttypes_0002', '2022-12-08 07:28:03.962194'),
(15, 'auth', '0007_alter_validators_add_error_messages', '2022-12-08 07:28:03.972165'),
(16, 'auth', '0008_alter_user_username_max_length', '2022-12-08 07:28:03.989106'),
(17, 'auth', '0009_alter_user_last_name_max_length', '2022-12-08 07:28:04.004787'),
(18, 'auth', '0010_alter_group_name_max_length', '2022-12-08 07:28:04.058160'),
(19, 'auth', '0011_update_proxy_permissions', '2022-12-08 07:28:04.267310'),
(20, 'auth', '0012_alter_user_first_name_max_length', '2022-12-08 07:28:04.290985'),
(21, 'sessions', '0001_initial', '2022-12-08 07:28:04.324861'),
(22, 'app', '0004_materiales', '2022-12-08 17:56:48.887721'),
(23, 'app', '0005_alter_materiales_imagen', '2022-12-08 18:07:39.230202');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('kctd48vsf9kif0ohq7qymyum7ag38l62', '.eJxVjEEOwiAUBe_C2pAipYBL9z0D-fAfUjU0Ke3KeHdt0oVu38y8lwi0rSVsDUuYWFyEEqffLVJ6oO6A71Rvs0xzXZcpyl2RB21ynBnP6-H-HRRq5Vtnr6wzlDV8BJCGs4NmhjPW2AGU2GV01lImA8fInTbKx77XYG2NF-8PFSA47w:1p3NvL:WLnCWmdVwnJwF_2wplUTrIzXgm0ruIR6q_EY_zUS9NQ', '2022-12-22 20:55:19.564857');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `db_carrotaller`
--
ALTER TABLE `db_carrotaller`
  ADD PRIMARY KEY (`id`),
  ADD KEY `db_carrotaller_taller_id_821ba4c1_fk_db_taller_codigo` (`taller_id`);

--
-- Indices de la tabla `db_items_taller`
--
ALTER TABLE `db_items_taller`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `db_materiales`
--
ALTER TABLE `db_materiales`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `db_postulacion`
--
ALTER TABLE `db_postulacion`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `db_reporte`
--
ALTER TABLE `db_reporte`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `db_taller`
--
ALTER TABLE `db_taller`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `db_taller_tipo_id_926a99c7_fk_db_tipo_taller_id_tipo` (`tipo_id`);

--
-- Indices de la tabla `db_tipo_taller`
--
ALTER TABLE `db_tipo_taller`
  ADD PRIMARY KEY (`id_tipo`);

--
-- Indices de la tabla `db_usuario`
--
ALTER TABLE `db_usuario`
  ADD PRIMARY KEY (`run`);

--
-- Indices de la tabla `db_usuario_administrador`
--
ALTER TABLE `db_usuario_administrador`
  ADD PRIMARY KEY (`run`);

--
-- Indices de la tabla `db_usuario_funcionario`
--
ALTER TABLE `db_usuario_funcionario`
  ADD PRIMARY KEY (`run`);

--
-- Indices de la tabla `db_usuario_instructor`
--
ALTER TABLE `db_usuario_instructor`
  ADD PRIMARY KEY (`run`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `db_carrotaller`
--
ALTER TABLE `db_carrotaller`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `db_items_taller`
--
ALTER TABLE `db_items_taller`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `db_carrotaller`
--
ALTER TABLE `db_carrotaller`
  ADD CONSTRAINT `db_carrotaller_taller_id_821ba4c1_fk_db_taller_codigo` FOREIGN KEY (`taller_id`) REFERENCES `db_taller` (`codigo`);

--
-- Filtros para la tabla `db_taller`
--
ALTER TABLE `db_taller`
  ADD CONSTRAINT `db_taller_tipo_id_926a99c7_fk_db_tipo_taller_id_tipo` FOREIGN KEY (`tipo_id`) REFERENCES `db_tipo_taller` (`id_tipo`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
