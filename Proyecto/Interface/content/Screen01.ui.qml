/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 2.6
import QtQuick.Controls 2.6
import "../Interface" as Interface

Rectangle {
    id: rectangle
    width: 1920
    height: 1080
    color: "#ffffff"
    property alias state0_0_text: state0_0.text
    property alias state1_0_text: state1_0.text
    property alias state2_0_text: state2_0.text
    property alias state3_0_text: state3_0.text

    property alias state0_1_text: state0_1.text
    property alias state1_1_text: state1_1.text
    property alias state2_1_text: state2_1.text
    property alias state3_1_text: state3_1.text

    property alias state0_2_text: state0_2.text
    property alias state1_2_text: state1_2.text
    property alias state2_2_text: state2_2.text
    property alias state3_2_text: state3_2.text

    property alias state0_3_text: state0_3.text
    property alias state1_3_text: state1_3.text
    property alias state2_3_text: state2_3.text
    property alias state3_3_text: state3_3.text

    property alias address0_0_text: address0_0.text
    property alias address1_0_text: address1_0.text
    property alias address2_0_text: address2_0.text
    property alias address3_0_text: address3_0.text

    property alias address0_1_text: address0_1.text
    property alias address1_1_text: address1_1.text
    property alias address2_1_text: address2_1.text
    property alias address3_1_text: address3_1.text

    property alias address0_2_text: address0_2.text
    property alias address1_2_text: address1_2.text
    property alias address2_2_text: address2_2.text
    property alias address3_2_text: address3_2.text

    property alias address0_3_text: address0_3.text
    property alias address1_3_text: address1_3.text
    property alias address2_3_text: address2_3.text
    property alias address3_3_text: address3_3.text

    property alias data0_0_text: data0_0.text
    property alias data1_0_text: data1_0.text
    property alias data2_0_text: data2_0.text
    property alias data3_0_text: data3_0.text

    property alias data0_1_text: data0_1.text
    property alias data1_1_text: data1_1.text
    property alias data2_1_text: data2_1.text
    property alias data3_1_text: data3_1.text

    property alias data0_2_text: data0_2.text
    property alias data1_2_text: data1_2.text
    property alias data2_2_text: data2_2.text
    property alias data3_2_text: data3_2.text

    property alias data0_3_text: data0_3.text
    property alias data1_3_text: data1_3.text
    property alias data2_3_text: data2_3.text
    property alias data3_3_text: data3_3.text

    property alias last_execution0_text: last_execution0.text
    property alias last_execution1_text: last_execution1.text
    property alias last_execution2_text: last_execution2.text
    property alias last_execution3_text: last_execution3.text

    property alias current_process0_text: current_process0.text
    property alias current_process1_text: current_process1.text
    property alias current_process2_text: current_process2.text
    property alias current_process3_text: current_process3.text

    property alias data_memory0_text:data_memory_0.text
    property alias data_memory1_text:data_memory_1.text
    property alias data_memory2_text:data_memory_2.text
    property alias data_memory3_text:data_memory_3.text
    property alias data_memory4_text:data_memory_4.text
    property alias data_memory5_text:data_memory_5.text
    property alias data_memory6_text:data_memory_6.text
    property alias data_memory7_text:data_memory_7.text

    property alias instruction_input_text:instruction_input.text

    signal buttonClick(string buttonId);


    Text {
        id: processor0
        x: 150
        y: 202
        text: qsTr("Procesador 0")
        font.pixelSize: 26
        renderType: Text.QtRendering
        font.bold: true
        scale: 1
    }
    
    Text {
        id: cache0
        x: 181
        y: 348
        text: qsTr("Cache 0")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Grid {
        id: cache1_grid
        x: 53
        y: 483
        width: 350
        height: 288
        opacity: 1
        visible: true
        leftPadding: 0
        clip: false
        transformOrigin: Item.Center
        smooth: true
        antialiasing: false
        spacing: 20
        verticalItemAlignment: Grid.AlignVCenter
        horizontalItemAlignment: Grid.AlignHCenter
        layoutDirection: Qt.LeftToRight
        flow: Grid.LeftToRight
        rows: 5
        columns: 4
        
        Text {
            id: block_number
            text: qsTr(" Bloque")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status
            text: qsTr("Estado")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address
            text: qsTr("Direccion")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum
            text: qsTr("Dato")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: block0_0
            text: qsTr("0")
            font.pixelSize: 19
        }
        
        Text {
            id: state0_0
            text: qsTr("Text")
            font.pixelSize: 19
            renderType: Text.QtRendering
        }
        
        Text {
            id: address0_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data0_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block1_0
            text: qsTr("1")
            font.pixelSize: 19
        }
        
        Text {
            id: state1_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address1_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data1_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block2_0
            text: qsTr("2")
            font.pixelSize: 19
        }
        
        Text {
            id: state2_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address2_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data2_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block3_0
            text: qsTr("3")
            font.pixelSize: 19
        }
        
        Text {
            id: state3_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address3_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data3_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
    }
    
    Grid {
        id: last_execution_grid
        x: 69
        y: 277
        width: 318
        height: 36
        spacing: 33
        rows: 1
        columns: 2
        
        Text {
            id: last_execution_label0
            width: 136
            height: 26
            text: qsTr("Ultima Ejecucion:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution0
            width: 136
            height: 26
            text: qsTr("Instruccion")
            font.pixelSize: 20
            renderType: Text.QtRendering
            font.bold: false
        }
    }
    
    Grid {
        id: process_grid0
        x: 78
        y: 406
        width: 318
        height: 36
        rows: 1
        spacing: 33
        Text {
            id: current_process_label0
            width: 136
            height: 26
            text: qsTr("Proceso actual")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: current_process0
            width: 136
            height: 26
            text: qsTr("proceso")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Text {
        id: processor1
        x: 610
        y: 202
        text: qsTr("Procesador 1")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Text {
        id: cache1
        x: 641
        y: 348
        text: qsTr("Cache 1")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Grid {
        id: cache1_grid1
        x: 513
        y: 483
        width: 350
        height: 288
        opacity: 1
        visible: true
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.LeftToRight
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        Text {
            id: block_number1
            text: qsTr(" Bloque")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status1
            text: qsTr("Estado")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address1
            text: qsTr("Direccion")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum1
            text: qsTr("Dato")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: block0_1
            text: qsTr("0")
            font.pixelSize: 19
        }
        
        Text {
            id: state0_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address0_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data0_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block1_1
            text: qsTr("1")
            font.pixelSize: 19
        }
        
        Text {
            id: state1_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address1_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data1_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block2_1
            text: qsTr("2")
            font.pixelSize: 19
        }
        
        Text {
            id: state2_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address2_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data2_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block3_1
            text: qsTr("3")
            font.pixelSize: 19
        }
        
        Text {
            id: state3_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address3_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data3_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        rows: 5
        smooth: true
        clip: false
        columns: 4
        spacing: 20
        antialiasing: false
    }
    
    Grid {
        id: last_execution_grid1
        x: 529
        y: 277
        width: 318
        height: 36
        rows: 1
        spacing: 33
        Text {
            id: last_execution_label1
            width: 136
            height: 26
            text: qsTr("Ultima Ejecucion:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution1
            width: 136
            height: 26
            text: qsTr("Instruccion")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Grid {
        id: process_grid1
        x: 538
        y: 406
        width: 318
        height: 36
        rows: 1
        spacing: 33
        Text {
            id: current_process_label1
            width: 136
            height: 26
            text: qsTr("Proceso actual")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: current_process1
            width: 136
            height: 26
            text: qsTr("proceso")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Text {
        id: processor2
        x: 1089
        y: 202
        text: qsTr("Procesador 2")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Text {
        id: cache2
        x: 1120
        y: 348
        text: qsTr("Cache 2")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Grid {
        id: cache1_grid2
        x: 992
        y: 483
        width: 350
        height: 288
        opacity: 1
        visible: true
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.LeftToRight
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        Text {
            id: block_number2
            text: qsTr(" Bloque")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status2
            text: qsTr("Estado")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address2
            text: qsTr("Direccion")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum2
            text: qsTr("Dato")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: block0_2
            text: qsTr("0")
            font.pixelSize: 19
        }
        
        Text {
            id: state0_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address0_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data0_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block1_2
            text: qsTr("1")
            font.pixelSize: 19
        }
        
        Text {
            id: state1_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address1_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data1_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block2_2
            text: qsTr("2")
            font.pixelSize: 19
        }
        
        Text {
            id: state2_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address2_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data2_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block3_2
            text: qsTr("3")
            font.pixelSize: 19
        }
        
        Text {
            id: state3_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address3_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data3_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        rows: 5
        smooth: true
        clip: false
        columns: 4
        antialiasing: false
        spacing: 20
    }
    
    Grid {
        id: last_execution_grid2
        x: 1008
        y: 277
        width: 318
        height: 36
        rows: 1
        spacing: 33
        Text {
            id: last_execution_label2
            width: 136
            height: 26
            text: qsTr("Ultima Ejecucion:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution2
            width: 136
            height: 26
            text: qsTr("Instruccion")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Grid {
        id: process_grid2
        x: 1017
        y: 406
        width: 318
        height: 36
        rows: 1
        spacing: 33
        Text {
            id: current_process_label2
            width: 136
            height: 26
            text: qsTr("Proceso actual")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: current_process2
            width: 136
            height: 26
            text: qsTr("proceso")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Text {
        id: processor3
        x: 1547
        y: 202
        text: qsTr("Procesador 3")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Text {
        id: cache3
        x: 1578
        y: 348
        text: qsTr("Cache 3")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Grid {
        id: cache1_grid3
        x: 1450
        y: 483
        width: 350
        height: 288
        opacity: 1
        visible: true
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.LeftToRight
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        Text {
            id: block_number3
            text: qsTr(" Bloque")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status3
            text: qsTr("Estado")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address3
            text: qsTr("Direccion")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum3
            text: qsTr("Dato")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: block0_3
            text: qsTr("0")
            font.pixelSize: 19
        }
        
        Text {
            id: state0_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address0_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data0_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block1_3
            text: qsTr("1")
            font.pixelSize: 19
        }
        
        Text {
            id: state1_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address1_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data1_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block2_3
            text: qsTr("2")
            font.pixelSize: 19
        }
        
        Text {
            id: state2_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address2_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data2_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: block3_3
            text: qsTr("3")
            font.pixelSize: 19
        }
        
        Text {
            id: state3_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: address3_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data3_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        rows: 5
        smooth: true
        clip: false
        columns: 4
        spacing: 20
        antialiasing: false
    }
    
    Grid {
        id: last_execution_grid3
        x: 1475
        y: 277
        width: 318
        height: 36
        rows: 1
        spacing: 33
        Text {
            id: last_execution_label3
            width: 136
            height: 26
            text: qsTr("Ultima Ejecucion:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution3
            width: 136
            height: 26
            text: qsTr("Instruccion")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Grid {
        id: process_grid3
        x: 1475
        y: 406
        width: 318
        height: 36
        rows: 1
        spacing: 33
        Text {
            id: current_process_label3
            width: 136
            height: 26
            text: qsTr("Proceso actual")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: current_process3
            width: 136
            height: 26
            text: qsTr("proceso")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Grid {
        id: memory_grid
        x: 655
        y: 904
        width: 543
        height: 91
        opacity: 1
        visible: true
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.TopToBottom
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        
        Text {
            id: direction_memory
            text: qsTr("Direccion")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: data_memory
            text: qsTr("Dato")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: direction_memory_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_4
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_4
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_5
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_5
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_6
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_6
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_7
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_7
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        rows: 2
        smooth: true
        clip: false
        columns: 17
        spacing: 20
        antialiasing: false
    }
    
    ToolSeparator {
        id: toolSeparator
        x: 453
        y: 202
        width: 34
        height: 569
    }
    
    ToolSeparator {
        id: toolSeparator1
        x: 923
        y: 202
        width: 34
        height: 569
    }
    
    ToolSeparator {
        id: toolSeparator2
        x: 1392
        y: 202
        width: 34
        height: 569
    }
    
    ToolSeparator {
        id: toolSeparator3
        x: 53
        y: 793
        width: 1747
        height: 36
        orientation: Qt.Horizontal
    }
    
    Text {
        id: memory_label
        x: 888
        y: 835
        text: qsTr("Memory")
        font.pixelSize: 26
        font.bold: true
        scale: 1
    }
    
    Grid {
        id: buttons
        x: 793
        y: 52
        width: 250
        height: 47
        rows: 1
        spacing: 48
        columns: 3
        
        Button {
            id: continue_btn
            width: 46
            height: 40
            visible: true
            checked: false
            display: AbstractButton.TextBesideIcon
            activeFocusOnTab: false
            focus: false
            antialiasing: false
            smooth: false
            enabled: true
            flat: false
            objectName: "continue_btn"

            BorderImage {
                id: borderImage
                height: 32
                opacity: 0.496
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                source: "../imgs/continue.png"
                enabled: true
                smooth: false
                activeFocusOnTab: true
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0
                horizontalTileMode: BorderImage.Round
            }


        }
        
        Button {
            id: step_btn
            width: 46
            height: 40
            flat: false
            objectName: "step_btn"
            BorderImage {
                id: borderImage1
                height: 32
                opacity: 0.496
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                source: "../imgs/step.png"
                horizontalTileMode: BorderImage.Round
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.rightMargin: 0
                anchors.topMargin: 0
            }
        }
        
        Button {
            id: stop_btn
            width: 46
            height: 40
            opacity: 1
            visible: false
            enabled: true
            flat: false
            objectName: "stop_btn"
            BorderImage {
                id: borderImage2
                height: 32
                opacity: 0.504
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                source: "../imgs/stop.jpg"
                horizontalTileMode: BorderImage.Round
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.rightMargin: 0
                anchors.topMargin: 0
            }
        }
    }
    
    Grid {
        id: instruction_input_grid
        x: 730
        y: 118
        width: 392
        height: 36
        rows: 1
        spacing: 50
        
        Text {
            id: instruction_input_label
            width: 136
            height: 26
            text: qsTr("Instruccion:")
            font.pixelSize: 20
            font.bold: false
        }
        
        TextInput {
            id: instruction_input
            width: 200
            height: 25
            text: qsTr("PX WRITE XXXX XXXX")
            font.pixelSize: 19
        }
        columns: 2
    }

    ToolSeparator {
        id: toolSeparator4
        x: 53
        y: 160
        width: 1747
        height: 36
        orientation: Qt.Horizontal
    }
    
    
    
    
    
    
}



/*##^##
Designer {
    D{i:0;annotation:"1 //;;//  //;;//  //;;// <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html> //;;// 1647079224";customId:"rectangulo";formeditorZoom:0.5}
}
##^##*/
