# -*- coding: utf-8 -*-
# NOMENCLATURAS
# TXT = Cajas de texto
# LBL = Labels
# OPT = Option button
# DPD = Select | Combo | Dropdown
# BTN = Botón

# TIPO DE OBJETO_NOMBRE_IDENTIFICADOR

class Registro:

    # -------------------- DATOS DE ENTRADA --------------------
    tituloPagina = "Registrarte con tu correo electrónico"
    emailUsuario = "testingUdemy@gmail.com"
    emailUsuarioConfirm = "testingUdemy@gmail.com"
    passwordUsuario = "testingPruebasUdem"
    aliasUsuario = "Clase44Udemy"

    # -------------------- LOCATORS --------------------
    # img_logo_xpath = ""

    lbl_titulo_xpath = "//h2[contains(.,'Registrarte con tu correo electrónico')]"

    txt_email_xpath = "//input[contains(@name,'email')]"

    txt_email_confirm_xpath = "//input[contains(@name,'confirm')]"

    txt_password_xpath = "password"
    txt_password_id = "password"

    txt_user_id = "displayname"


