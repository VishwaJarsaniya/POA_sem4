DATA SEGMENT
    N1 DB 40H
    N2 DB 30H
    ADD_RES DB ?
    SUB_RES DB ?
DATA ENDS

CODE SEGMENT
ASSUME: CS:CODE,DS:DATA

START:
MOV AX,DATA
MOV DS,AX

CALL ADDITION
CALL SUBTRACTION

MOV AH,4CH
INT 21H


ADDITION PROC NEAR
    MOV AL,N1
    MOV BL,N2
    ADD AL,BL
    MOV ADD_RES,AL
    RET
ADDITION ENDP

SUBTRACTION PROC NEAR
    MOV AL,N1
    MOV BL,N2
    SUB AL,BL
    MOV SUB_RES,AL
    RET
SUBTRACTION ENDP

CODE ENDS
END START