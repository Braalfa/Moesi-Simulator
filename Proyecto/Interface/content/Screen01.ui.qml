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
    width: 1400
    height: 900
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

    property alias data_memory0_text:data_memory_0.text
    property alias data_memory1_text:data_memory_1.text
    property alias data_memory2_text:data_memory_2.text
    property alias data_memory3_text:data_memory_3.text
    property alias data_memory4_text:data_memory_4.text
    property alias data_memory5_text:data_memory_5.text
    property alias data_memory6_text:data_memory_6.text
    property alias data_memory7_text:data_memory_7.text

    property alias instruction_input_text:instruction_input.text

    property alias current_process0_text: current_process0.text
    property alias current_process1_text: current_process1.text
    property alias current_process2_text: current_process2.text
    property alias current_process3_text: current_process3.text



    signal buttonClick(string buttonId);

    Text {
        id: current_process_label0
        x: 107
        y: 324
        width: 136
        height: 26
        text: qsTr("State:")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Text {
        id: current_process0
        x: 243
        y: 325
        width: 136
        height: 26
        text: qsTr("state")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Text {
        id: processor0
        x: 150
        y: 202
        text: qsTr("Processor 0")
        font.pixelSize: 26
        renderType: Text.QtRendering
        font.bold: true
        scale: 0.7
    }
    
    Text {
        id: cache0
        x: 165
        y: 392
        text: qsTr("Cache 0")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Grid {
        id: cache1_grid
        x: 62
        y: 401
        width: 350
        height: 288
        opacity: 1
        visible: true
        scale: 0.7
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
            text: qsTr(" Block")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status
            text: qsTr("State")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address
            text: qsTr("Direction")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum
            text: qsTr("Data")
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
        scale: 0.7
        spacing: 33
        rows: 1
        columns: 2
        
        Text {
            id: last_execution_label0
            width: 136
            height: 26
            text: qsTr("Latest instruction:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution0
            width: 136
            height: 26
            text: qsTr("Instruction")
            font.pixelSize: 20
            renderType: Text.QtRendering
            font.bold: false
        }
    }
    
    Grid {
        id: process_grid0
        x: 101
        y: 319
        width: 318
        height: 36
        scale: 0.7
        rows: 1
        spacing: 33
        columns: 2
    }
    
    Text {
        id: processor1
        x: 474
        y: 196
        text: qsTr("Processor 1")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Text {
        id: cache1
        x: 489
        y: 386
        text: qsTr("Cache 1")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Grid {
        id: cache1_grid1
        x: 386
        y: 396
        width: 350
        height: 288
        opacity: 1
        visible: true
        scale: 0.7
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.LeftToRight
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        Text {
            id: block_number1
            text: qsTr(" Block")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status1
            text: qsTr("State")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address1
            text: qsTr("Direction")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum1
            text: qsTr("Data")
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
        x: 393
        y: 271
        width: 318
        height: 36
        scale: 0.7
        rows: 1
        spacing: 33
        Text {
            id: last_execution_label1
            width: 136
            height: 26
            text: qsTr("Latest instruction:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution1
            width: 136
            height: 26
            text: qsTr("Instruction")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Text {
        id: processor2
        x: 790
        y: 199
        text: qsTr("Processor 2")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Text {
        id: cache2
        x: 805
        y: 389
        text: qsTr("Cache 2")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Grid {
        id: cache1_grid2
        x: 702
        y: 399
        width: 350
        height: 288
        opacity: 1
        visible: true
        scale: 0.7
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.LeftToRight
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        Text {
            id: block_number2
            text: qsTr(" Block")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status2
            text: qsTr("State")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address2
            text: qsTr("Direction")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum2
            text: qsTr("Data")
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
        x: 709
        y: 274
        width: 318
        height: 36
        scale: 0.7
        rows: 1
        spacing: 33
        Text {
            id: last_execution_label2
            width: 136
            height: 26
            text: qsTr("Latest instruction:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution2
            width: 136
            height: 26
            text: qsTr("Instruction")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Text {
        id: processor3
        x: 1103
        y: 198
        text: qsTr("Processor 3")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Text {
        id: cache3
        x: 1118
        y: 388
        text: qsTr("Cache 3")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Grid {
        id: cache1_grid3
        x: 1015
        y: 398
        width: 350
        height: 288
        opacity: 1
        visible: true
        scale: 0.7
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.LeftToRight
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        Text {
            id: block_number3
            text: qsTr(" Block")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: status3
            text: qsTr("State")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: address3
            text: qsTr("Direction")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: datum3
            text: qsTr("Data")
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
        x: 1031
        y: 273
        width: 318
        height: 36
        scale: 0.7
        rows: 1
        spacing: 33
        Text {
            id: last_execution_label3
            width: 136
            height: 26
            text: qsTr("Latest instruction:")
            font.pixelSize: 20
            font.bold: false
        }
        
        Text {
            id: last_execution3
            width: 136
            height: 26
            text: qsTr("Instruction")
            font.pixelSize: 20
            font.bold: false
        }
        columns: 2
    }
    
    Grid {
        id: memory_grid
        x: 76
        y: 86
        width: 543
        height: 91
        opacity: 1
        visible: true
        scale: 0.7
        verticalItemAlignment: Grid.AlignVCenter
        flow: Grid.TopToBottom
        leftPadding: 0
        horizontalItemAlignment: Grid.AlignHCenter
        transformOrigin: Item.Center
        layoutDirection: Qt.LeftToRight
        
        Text {
            id: direction_memory
            text: qsTr("Direction")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: data_memory
            text: qsTr("Data")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            font.bold: true
        }
        
        Text {
            id: direction_memory_0
            text: qsTr("000")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_0
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_1
            text: qsTr("001")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_1
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_2
            text: qsTr("010")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_2
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_3
            text: qsTr("011")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_3
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_4
            text: qsTr("100")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_4
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_5
            text: qsTr("101")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_5
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_6
            text: qsTr("110")
            font.pixelSize: 19
        }
        
        Text {
            id: data_memory_6
            text: qsTr("Text")
            font.pixelSize: 19
        }
        
        Text {
            id: direction_memory_7
            text: qsTr("111")
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
        x: 368
        y: 125
        width: 34
        height: 569
        scale: 0.7
    }
    
    ToolSeparator {
        id: toolSeparator1
        x: 696
        y: 116
        width: 34
        height: 569
        scale: 0.7
    }
    
    ToolSeparator {
        id: toolSeparator2
        x: 1008
        y: 116
        width: 34
        height: 569
        scale: 0.7
    }
    
    ToolSeparator {
        id: toolSeparator3
        x: -155
        y: 642
        width: 1747
        height: 36
        scale: 0.7
        orientation: Qt.Horizontal
    }
    
    Text {
        id: memory_label
        x: 309
        y: 17
        text: qsTr("Memory")
        font.pixelSize: 26
        font.bold: true
        scale: 0.7
    }
    
    Grid {
        id: buttons
        x: 614
        y: 55
        width: 250
        height: 47
        scale: 0.7
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
                scale: 0.7
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
                scale: 0.7
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
                scale: 0.7
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
        x: 528
        y: 117
        width: 392
        height: 36
        scale: 0.7
        rows: 1
        spacing: 50
        
        Text {
            id: instruction_input_label
            width: 136
            height: 26
            text: qsTr("Instruction:")
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
        x: -155
        y: 164
        width: 1747
        height: 36
        scale: 0.7
        orientation: Qt.Horizontal
    }

    Text {
        id: current_process_label1
        x: 431
        y: 318
        width: 136
        height: 26
        text: qsTr("State:")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Text {
        id: current_process1
        x: 567
        y: 319
        width: 136
        height: 26
        text: qsTr("state")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Grid {
        id: process_grid1
        x: 425
        y: 313
        width: 318
        height: 36
        scale: 0.7
        rows: 1
        spacing: 33
        columns: 2
    }

    Text {
        id: current_process_label2
        x: 755
        y: 322
        width: 136
        height: 26
        text: qsTr("State:")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Text {
        id: current_process2
        x: 891
        y: 323
        width: 136
        height: 26
        text: qsTr("state")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Grid {
        id: process_grid2
        x: 749
        y: 317
        width: 318
        height: 36
        scale: 0.7
        rows: 1
        spacing: 33
        columns: 2
    }

    Text {
        id: current_process_label3
        x: 1084
        y: 319
        width: 136
        height: 26
        text: qsTr("State:")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Text {
        id: current_process3
        x: 1220
        y: 320
        width: 136
        height: 26
        text: qsTr("state")
        font.pixelSize: 20
        scale: 0.7
        font.bold: false
    }

    Grid {
        id: process_grid3
        x: 1078
        y: 314
        width: 318
        height: 36
        scale: 0.7
        rows: 1
        spacing: 33
        columns: 2
    }
    
    
    
    
    
    
}



/*##^##
Designer {
    D{i:0;formeditorZoom:0.25}
}
##^##*/
