import numpy as np

def verificar_data_drift(temperaturas, umidades):
    """
    Realiza a auditoria de dados comparando a média e a volatilidade (desvio padrão)
    das amostras de temperatura e umidade.
    """
    # Exemplo de lógica de média que já existia (calculada via numpy para consistência)
    media_temp = np.mean(temperaturas)
    media_umid = np.mean(umidades)
    
    # --- REFATORAÇÃO ESTATÍSTICA SOLICITADA ---
    # 1. Cálculo do Desvio Padrão utilizando numpy
    std_temp = np.std(temperaturas)
    std_umid = np.std(umidades)
    
    print(f"[Auditoria] Média Temp: {media_temp:.2f}°C | Desvio Padrão Temp: {std_temp:.2f}°C")
    print(f"[Auditoria] Média Umid: {media_umid:.2f}% | Desvio Padrão Umid: {std_umid:.2f}%")
    
    # 2. Critério de Rejeição por Volatilidade
    if std_temp > 5.0 or std_umid > 15.0:
        print("[ALERTA CRÍTICO] Alta volatilidade detectada nos sensores!")
        return False
        
    # Se passar na volatilidade, o fluxo segue normal
    return True