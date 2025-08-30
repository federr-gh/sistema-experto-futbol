import clips

env = clips.Environment()

def inicializar_clips():
    env.build("(deftemplate Equipo_estado (slot Equipo_A_estado (type SYMBOL)))")
    env.build("(deftemplate Rival_estado (slot Equipo_B_estado (type SYMBOL)))")
    env.build("(deftemplate Tiempo (slot Tiempo_restante (type SYMBOL)))")
    env.build("(deftemplate Estrategia (slot Estrategia_equipo_A (type SYMBOL)))")

    env.build("(defrule Equipo_A_perdiendo_tiempo_corto (Equipo_estado (Equipo_A_estado perdiendo)) (Tiempo (Tiempo_restante corto)) => (assert (Estrategia (Estrategia_equipo_A todos_arriba))))")
    env.build("(defrule Equipo_A_ganando_por_1_gol_tiempo_largo (Equipo_estado (Equipo_A_estado ganando_por_1_gol)) (Tiempo (Tiempo_restante largo)) => (assert (Estrategia (Estrategia_equipo_A posesion_del_balon))))")
    env.build("(defrule Equipo_A_ganando_por_3_goles (Equipo_estado (Equipo_A_estado ganando_por_3_goles)) => (assert (Estrategia (Estrategia_equipo_A defensa_solida))))")
    env.build("(defrule Equipo_A_delanteros_rapidos_Equipo_B_defensas_lentos (Equipo_estado(Equipo_A_estado delanteros_rapidos))(Rival_estado(Equipo_B_estado defensas_lentos)) => (assert (Estrategia(Estrategia_equipo_A todos_arriba))))")
    env.build("(defrule Equipo_A_mediocampistas_creativos_Equipo_B_mediocampo_debil (Equipo_estado (Equipo_A_estado mediocampistas_creativos)) (Rival_estado(Equipo_B_estado mediocampo_debil)) => (assert (Estrategia (Estrategia_equipo_A posesion_del_balon))))")
    env.build("(defrule Equipo_A_defensa_fuerte_Equipo_B_delanteros_debiles (Equipo_estado (Equipo_A_estado defensa_fuerte)) (Rival_estado(Equipo_B_estado  delanteros_debiles)) => (assert (Estrategia (Estrategia_equipo_A defensa_solida))))")

    #Hechos
    env.assert_string("(Equipo_estado (Equipo_A_estado perdiendo))")
    env.assert_string("(Tiempo (Tiempo_restante corto))")
    env.assert_string("(Equipo_estado (Equipo_A_estado ganando_por_1_gol))")
    env.assert_string("(Tiempo (Tiempo_restante largo))")
    env.assert_string("(Equipo_estado (Equipo_A_estado ganando_por_3_goles))")
    env.assert_string("(Equipo_estado (Equipo_A_estado delanteros_rapidos))")
    env.assert_string("(Rival_estado (Equipo_B_estado defensas_lentos))")
    env.assert_string("(Equipo_estado (Equipo_A_estado mediocampistas_creativos))")
    env.assert_string("(Rival_estado (Equipo_B_estado mediocampo_debil))")
    env.assert_string("(Equipo_estado (Equipo_A_estado defensa_fuerte))")
    env.assert_string("(Rival_estado (Equipo_B_estado delanteros_debiles))")


