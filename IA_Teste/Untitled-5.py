if __name__ == "__main__":
    print("=== INICIANDO PIPELINE DE AUDITORIA DE IA ===")
    
    # --- Cenário da ETAPA 2 (Simulação de execução dos Lotes) ---
    print("\n[Executando Auditoria do Lote 3...]")
    # Dados absurdos do Lote 3 citados no enunciado (ex: 5°C e 45°C)
    temperaturas_lote3 = [5.0, 25.0, 45.0, 25.0] 
    umidades_lote3 = [60.0, 62.0, 59.0, 61.0]
    
    # Deve printar o Alerta Crítico e retornar False
    lote3_valido = verificar_data_drift(temperaturas_lote3, umidades_lote3)
    
    # --- Cenário da ETAPA 3 (Execução do Cenário Metamórfico B) ---
    print("\n[Executando Cenário Metamórfico B...]")
    # Umidade subindo de 75% para 90% com temperatura fixa em 35°C
    risco_b_inicial = modelo_bayesiano_risco_clima(35.0, 75.0)
    risco_b_final = modelo_bayesiano_risco_clima(35.0, 90.0)
    print(f"Cenário B - Risco Inicial (Umid 75%): {risco_b_inicial:.2f}%")
    print(f"Cenário B - Risco Final (Umid 90%): {risco_b_final:.2f}% (Limitado e Realista)")

    # --- Cenário da ETAPA 4 (Invocação do Novo Teste Metamórfico) ---
    # Instancia a classe ou chama diretamente o método criado
    testador = TestadorClimaticoMetamorfico()
    
    # Executa o teste com uma umidade fixa (ex: 80%) e temperatura base (ex: 30°C)
    testador.testar_relacao_metamorfica_temperatura(umidade_fixa=80.0, temp_base=30.0)
    
    print("\n=== PIPELINE DE AUDITORIA CONCLUÍDO ===")