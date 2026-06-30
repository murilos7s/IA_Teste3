class TestadorClimaticoMetamorfico:
    # ... (outros métodos da classe de teste)

    def testar_relacao_metamorfica_temperatura(self, umidade_fixa: float, temp_base: float):
        """
        Garante a lei física invariante: se a temperatura sobe, 
        o risco deve subir ou se manter estável.
        """
        print(f"\n--- Iniciando Teste Metamórfico de Temperatura ---")
        print(f"Parâmetros Iniciais: Umidade Fixa = {umidade_fixa}%, Temperatura Base = {temp_base}°C")
        
        # 1. Calcula o risco para a situação base
        risco_base = modelo_bayesiano_risco_clima(temp_base, umidade_fixa)
        
        # 2. Aplica a transformação metamórfica (+5°C na temperatura)
        temp_alterada = temp_base + 5.0
        risco_alterado = modelo_bayesiano_risco_clima(temp_alterada, umidade_fixa)
        
        print(f"Risco Base (Temp {temp_base}°C): {risco_base:.2f}%")
        print(f"Risco Alterado (Temp {temp_alterada}°C): {risco_alterado:.2f}%")
        
        # 3. Validação do Par Metamórfico (Risco Alterado >= Risco Base)
        if risco_alterado >= risco_base:
            print("✓ [SUCESSO] Teste Metamórfico Passou: O risco subiu ou se manteve estável.")
            return True
        else:
            print("X [FALHA] Teste Metamórfico Falhou: Risco diminuiu com o aumento da temperatura!")
            return False