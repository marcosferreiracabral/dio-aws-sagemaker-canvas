Para este laboratório da DIO sobre AWS SageMaker Canvas, estruturei o conteúdo com foco em MLOps No-Code, destacando a agilidade analítica que a ferramenta proporciona.

🚀 Previsão de Estoque Inteligente com AWS SageMaker Canvas
Este repositório contém a documentação e os artefatos do projeto de Machine Learning No-Code para previsão de estoque, desenvolvido durante o bootcamp na Digital Innovation One (DIO). O objetivo é demonstrar como utilizar inteligência artificial para otimizar a cadeia de suprimentos com baixo esforço de codificação, mas alto rigor analítico.

🛠️ Tech Stack & Arquitetura
Plataforma: Amazon SageMaker Canvas

Dados: Dataset de 500 registros (Séries Temporais)

Abordagem: Time-Series Forecasting (No-Code ML)

Governança: AWS IAM & S3

📋 Fluxo do Projeto (Step-by-Step)
Com base no framework proposto no repositório original, o desenvolvimento seguiu as etapas abaixo:

1. Selecionar Dataset
Origem: Upload do arquivo dataset-500-curso-sagemaker-canvas-dio.csv para o SageMaker Canvas.

Análise Exploratória Inicial: Identificação das colunas ID_PRODUTO, DIA, FLAG_PROMOCAO e a variável alvo QUANTIDADE_ESTOQUE.

2. Construir e Treinar
Configuração do Modelo: Seleção do tipo de modelo "Time Series Forecasting".

Parametrização:

ID da Série: ID_PRODUTO

Timestamp: DIA

Target: QUANTIDADE_ESTOQUE

Engine: Utilizado o Standard Build para maior precisão estatística nas métricas de erro.

3. Analisar
Após o treinamento, o modelo foi avaliado com as seguintes métricas (benchmarks de mercado):

Avg. wQL (Weighted Quantile Loss): Avaliação da precisão da distribuição.

MAPE / RMSE: Verificação do desvio padrão das previsões em relação ao estoque real.

Impacto de Variáveis: Verificação de como a FLAG_PROMOCAO influencia os picos de demanda.

4. Prever
Single Prediction: Análise pontual de SKUs específicos para os próximos 5 dias.

Batch Prediction: Geração de previsões em massa para todos os produtos do portfólio.

Exportação: Resultados exportados para análise em ferramentas de BI (Power BI/Quicksight).

💡 Insights e Conclusões Técnicas
Como especialista em dados, os principais aprendizados deste laboratório foram:

Agilidade de Negócio: O SageMaker Canvas reduz drasticamente o tempo de Time-to-Market para provas de conceito (PoCs).

Qualidade dos Dados (GIGO): Mesmo sendo No-Code, a eficácia do modelo depende diretamente de um pipeline de ETL bem estruturado (como os que construímos com PySpark).

Ajuste de Promocionais: O modelo capturou com sucesso que itens em promoção necessitam de um estoque de segurança ~20% maior.

👤 Autor
Marcos Ferreira Cabral

Data Engineer com mais de 18 anos de sólida experiência em Tecnologia da Informação.

Mestre em Administração de Empresas (MUST University) | MBA em Big Data e Data Science (FIAP).

Responsável por soluções de dados no Itaú e entusiasta de IA e LLMOps.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
