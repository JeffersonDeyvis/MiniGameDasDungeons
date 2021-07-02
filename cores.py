#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lista_cores = [("azul",'\033[34m'), ("amarelo",'\033[33m'), ("vermelho",'\033[31m'),("verde",'\033[32m'),("ciano",'\033[36m'),("magenta",'\033[35m'),("amarelo",'\033[33m'),("preto",'\033[30m'),("branco",'\033[37m'),("original",'\033[0;0m')]
cor = dict(lista_cores)

lista_fundo = [("f_branco ",'\033[47m'),("f_preto",'\033[40m'),("f_vermelho",'\033[41m'),("f_verde",'\033[42m'),("f_amarelo",'\033[43m'),("f_azul",'\033[44m'),("f_magenta",'\033[45m'),("f_ciano",'\033[46m'),("f_branco",'\033[47m')]
fundo = dict(lista_fundo)

def colors(bg_color,text_color,string):
    F = str("f_"+ bg_color)
    C = text_color
    r = (fundo[F] + cor[C] + string + cor["original"])
    return r




