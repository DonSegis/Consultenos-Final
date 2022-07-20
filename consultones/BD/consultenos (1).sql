-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-07-2022 a las 10:20:08
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
-- Base de datos: `consultenos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `areaticket`
--

CREATE TABLE `areaticket` (
  `id_area` int(11) NOT NULL,
  `Area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `areaticket`
--

INSERT INTO `areaticket` (`id_area`, `Area`) VALUES
(1, 'Area 1'),
(2, 'Area 2'),
(3, 'Area 3'),
(4, 'Area 4'),
(5, 'Sin Area');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadoticket`
--

CREATE TABLE `estadoticket` (
  `Id_estado` int(11) NOT NULL,
  `Estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadoticket`
--

INSERT INTO `estadoticket` (`Id_estado`, `Estado`) VALUES
(1, 'Revision'),
(2, 'Resuelto'),
(3, 'No Aplicable');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ticket`
--

CREATE TABLE `ticket` (
  `Id_ticket` int(11) NOT NULL,
  `Nombre_cliente` varchar(50) NOT NULL,
  `Rut_cliente` varchar(12) NOT NULL,
  `Fecha` date NOT NULL,
  `Telefono` varchar(10) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `Criticidad` varchar(50) NOT NULL,
  `Detalles_servicio` varchar(200) NOT NULL,
  `Detalles_problema` varchar(200) NOT NULL,
  `observación` varchar(100) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_area` int(11) NOT NULL,
  `Id_estado` int(11) NOT NULL,
  `id_tipoTicket` int(11) NOT NULL,
  `id_usuarioCierre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoticket`
--

CREATE TABLE `tipoticket` (
  `id_tipoTicket` int(11) NOT NULL,
  `Tipo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipoticket`
--

INSERT INTO `tipoticket` (`id_tipoTicket`, `Tipo`) VALUES
(1, 'Felicitación'),
(2, 'Consulta'),
(3, 'Reclamo'),
(4, 'Problema');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipousuario`
--

CREATE TABLE `tipousuario` (
  `id_tipoUser` int(11) NOT NULL,
  `tipoUsuario` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipousuario`
--

INSERT INTO `tipousuario` (`id_tipoUser`, `tipoUsuario`) VALUES
(1, 'jefe ejecutivo'),
(2, 'ejecutivo de area'),
(3, 'operador de mesa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `rut` varchar(12) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Contaseña` varchar(30) NOT NULL,
  `id_tipoUser` int(11) NOT NULL,
  `id_area` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `rut`, `Nombre`, `Apellido`, `Contaseña`, `id_tipoUser`, `id_area`) VALUES
(1, '21.140.324-1', 'Sebastian', 'Norero', '123456gato', 1, 5),
(2, '10.524.843-1', 'Alvaro', 'Alvarez', '123456perro', 2, 1),
(3, '12.670.479-8', 'Maria', 'Diaz', '123456pez', 3, 5),
(4, '12.456.789-4', 'Pablo', 'Puertas', '123456', 3, 5),
(5, '12.345.678-9', 'Benjamin', 'Perez', '123456', 2, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `areaticket`
--
ALTER TABLE `areaticket`
  ADD PRIMARY KEY (`id_area`);

--
-- Indices de la tabla `estadoticket`
--
ALTER TABLE `estadoticket`
  ADD PRIMARY KEY (`Id_estado`);

--
-- Indices de la tabla `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`Id_ticket`),
  ADD UNIQUE KEY `FK_id_usuarioCierre` (`id_usuarioCierre`),
  ADD KEY `FK_id_usuario` (`id_usuario`),
  ADD KEY `FK_id_area` (`id_area`),
  ADD KEY `FK_id_estado` (`Id_estado`),
  ADD KEY `FK_id_tipoTicket` (`id_tipoTicket`);

--
-- Indices de la tabla `tipoticket`
--
ALTER TABLE `tipoticket`
  ADD PRIMARY KEY (`id_tipoTicket`);

--
-- Indices de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  ADD PRIMARY KEY (`id_tipoUser`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `FK_id_tipoUser` (`id_tipoUser`),
  ADD KEY `FK_id_area` (`id_area`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `areaticket`
--
ALTER TABLE `areaticket`
  MODIFY `id_area` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `estadoticket`
--
ALTER TABLE `estadoticket`
  MODIFY `Id_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `ticket`
--
ALTER TABLE `ticket`
  MODIFY `Id_ticket` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipoticket`
--
ALTER TABLE `tipoticket`
  MODIFY `id_tipoTicket` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  MODIFY `id_tipoUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
