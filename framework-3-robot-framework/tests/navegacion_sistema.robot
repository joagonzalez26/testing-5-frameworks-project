*** Settings ***
Library    SeleniumLibrary

Suite Setup       Abrir Navegador
Suite Teardown    Cerrar Navegador
Test Setup        Ir Al Inicio

*** Variables ***
${URL}        http://localhost:5173
${BROWSER}    Chrome

*** Test Cases ***
RF-001 - Verificar Carga Del Frontend
    [Documentation]    Valida que la aplicación web cargue correctamente desde el navegador.
    Page Should Contain    Dashboard
    Capture Page Screenshot    robot-frontend-home.png

RF-002 - Verificar Navegacion A Participantes
    [Documentation]    Valida que el módulo Participantes sea accesible desde la interfaz.
    Click Menu Option    Participantes
    Page Should Contain    Participantes
    Capture Page Screenshot    robot-participantes.png

RF-003 - Verificar Navegacion A Salas
    [Documentation]    Valida que el módulo Salas sea accesible desde la interfaz.
    Click Menu Option    Salas
    Page Should Contain    Salas
    Capture Page Screenshot    robot-salas.png

RF-004 - Verificar Navegacion A Reservas
    [Documentation]    Valida que el módulo Reservas sea accesible desde la interfaz.
    Click Menu Option    Reservas
    Page Should Contain    Reservas
    Capture Page Screenshot    robot-reservas.png

RF-005 - Verificar Navegacion A Reportes
    [Documentation]    Valida que el módulo Reportes sea accesible desde la interfaz.
    Click Menu Option    Reportes
    Page Should Contain    Reportes
    Capture Page Screenshot    robot-reportes.png

RF-006 - Verificar Error En Modulo Sanciones
    [Documentation]    Valida que el módulo Sanciones muestra un error visible ya detectado en la exploración manual.
    Click Menu Option    Sanciones
    Page Should Contain    Sanciones
    Wait Until Page Contains    Error    timeout=10 seconds
    Capture Page Screenshot    robot-sanciones-error.png

RF-007 - Verificar Error En Dashboard
    [Documentation]    Valida el error visible en la sección de horarios más demandados del Dashboard.
    Page Should Contain    Dashboard
    Wait Until Page Contains    Error cargando horarios    timeout=10 seconds
    Capture Page Screenshot    robot-dashboard-error-horarios.png

*** Keywords ***
Abrir Navegador
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    10 seconds
    Set Screenshot Directory    framework-3-robot-framework/evidencias
    Register Keyword To Run On Failure    Capture Page Screenshot

Cerrar Navegador
    Close Browser

Ir Al Inicio
    Go To    ${URL}
    Wait Until Page Contains    Dashboard    timeout=10 seconds

Click Menu Option
    [Arguments]    ${texto}
    ${xpath}=    Set Variable    xpath=//a[contains(normalize-space(.), "${texto}")] | //button[contains(normalize-space(.), "${texto}")] | //div[contains(normalize-space(.), "${texto}")]
    Wait Until Element Is Visible    ${xpath}    timeout=10 seconds
    Click Element    ${xpath}
    Sleep    1 second