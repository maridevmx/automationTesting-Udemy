# Created by Herbig-Haro at 22/07/2020
@Selenium
Feature: Funciones básicas de Selenium con BDD
  # Enter feature description here

  @Navegador
  Scenario: Abrir el navegador
    Given Abrir la aplicacion

  @Navegador
  Scenario: Abrir con URL
    Given Inicializo la app en la URL https://www.toolsqa.com/cucumber/behavior-driven-development/
    Then Cierro la app

  @Navegador
  Scenario: Abrir con navegador
    Given Abro la app con el navegador CHROME
    Then Cierro la app

  @FuncionesSelenium
  @DOM
  Scenario: Establecer el DOM
    Given Abrir la aplicacion
    And Cargo el DOM de la App: spotify_registro
    And En el campo Email se escribe testingUdemy@gmail.com
    And Se captura pantalla: EmailSpotify
    Then Cierro la app

  @Captura
  Scenario: Tomar captura de pantalla
    Given Abrir la aplicacion
    And Cargo el DOM de la App: spotify_registro
    And En el campo Email se escribe testingUdemy@gmail.com
    And Se toma captura de pantalla TestUdemy
    Then Cierro la app

  @TextboxDropdown
  Scenario: Clics Dropdowns y textbox
    Given Abrir la aplicacion
    And Cargo el DOM de la App: spotify_registro
    And En el campo Email se escribe testingUdemy@gmail.com
    And En el dropdown Mes de nacimiento se selecciona Septiembre
    Then Cierro la app

  Scenario: Frames y Ventanas
    Given Inicializo la app en la URL https://chercher.tech/practice/frames-example-selenium-webdriver
    And Cargo el DOM de la App: frames
    And Se realiza un desplazamiento al frame: Frame2
    And En el dropdown Frame2 Select se selecciona Avatar
    And Se regresa al Frame Padre
    And Se realiza un desplazamiento al frame: Frame1
    And En el campo Frame1 Input se escribe Hola Chicos Udemy
    And Se realiza un desplazamiento al frame: Frame3
    And Se realiza un click en Frame3 Input
    And Se toma captura de pantalla Test004
    Then Cierro la app

  Scenario: Busqueda de texto en Spotify
    Given Abrir la aplicacion
    And Cargo el DOM de la App: spotify_registro
    And Se realiza un scroll hacia el elemento: verifica_cuenta
    And Se realiza clic en el texto: Inicia ses
    And Esperar que finalice la carga de la pagina
    Then Cierro la app
