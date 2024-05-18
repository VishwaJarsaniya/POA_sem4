DATA SEGMENT
    S1 DB 05H,08H,07H,04H,01H
    LEN DB 5
    SUM DW ?
    AVG DW ?
DATA ENDS

CODE SEGMENT
ASSUME CS:CODE, DS:DATA       

START:
MOV AX,DATA
MOV DS,AX
LEA SI,S1
MOV AX,00H     
MOV CL,LEN

REPEAT:
MOV BL,[SI]
ADD AL,BL
INC SI
DEC CL
JNZ REPEAT

MOV SUM,AX
DIV LEN
MOV AVG,AX

CODE ENDS
END START