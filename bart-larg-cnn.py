from transformers import pipeline
import time

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ O Traefik é um moderno balanceador de carga (load balancer) e proxy reverso desenvolvido especialmente para ambientes de contêineres. Em poucas palavras, ele facilita o gerenciamento de tráfego em suas aplicações, distribuindo as solicitações dos usuários entre diferentes servidores ou instâncias de aplicativos para garantir desempenho e confiabilidade.
Por que Traefik é Especial? Integração Simples: Uma das razões pelas quais o Traefik é tão popular é sua integração fácil com várias plataformas de orquestração de contêineres, como Docker, Kubernetes e Swarm. Ele pode se adaptar dinamicamente às mudanças na sua infraestrutura, algo vital em ambientes de contêineres onde as instâncias podem ser escaladas para cima ou para baixo rapidamente.
Configuração Automática: O Traefik é inteligente. Ele pode descobrir automaticamente novos serviços e ajustar sua configuração em conformidade, economizando tempo e esforço para os desenvolvedores.
Suporte para Protocolos Modernos: Ele não apenas manipula o HTTP/HTTPS tradicional, mas também oferece suporte para protocolos modernos como gRPC e WebSockets, o que o torna uma escolha robusta para aplicativos avançados.
Segurança em Primeiro Lugar: A segurança é uma prioridade para o Traefik. Ele vem com suporte nativo para SSL/TLS, facilitando a implementação de comunicações seguras em sua aplicação.
"""

ARTICLE2 = """Interpretação de texto
Interpretação de texto é a habilidade de compreender e extrair significado a partir de um texto escrito. Isso envolve não apenas entender as palavras individualmente, mas também compreender o contexto, as ideias apresentadas, as relações entre as palavras e frases, e inferir informações implícitas que podem não estar claramente expressas no texto. É uma habilidade essencial em várias situações, como em concursos, exames, estudos acadêmicos e na vida cotidiana.
Aqui estão algumas dicas para melhorar suas habilidades de interpretação de texto:
Leitura Cuidadosa: Leia o texto cuidadosamente, prestando atenção às palavras, frases e parágrafos. Não tenha pressa; compreensão requer tempo e concentração.
Identifique o Tema: Descubra qual é o tema central do texto. Isso ajuda a entender o propósito do autor e a organização das informações no texto.
Faça Perguntas: Faça perguntas sobre o texto. Quem são os personagens? Qual é o conflito? Qual é a mensagem principal? Questionar o texto ajuda a extrair significado mais profundo.
Note Detalhes: Preste atenção aos detalhes no texto, como exemplos, estatísticas ou citações. Eles podem fornecer informações importantes para entender o contexto.
Inferências: Faça inferências com base no que está escrito e no seu conhecimento prévio. Às vezes, as informações implícitas são tão cruciais quanto as explícitas.
Contexto: Considere o contexto do texto, incluindo o período em que foi escrito e o autor. Isso pode fornecer insights valiosos sobre o significado do texto.
Prática Regular: A prática constante é fundamental para a melhoria. Leia uma variedade de textos, desde artigos de jornais até literatura, para desenvolver suas habilidades de interpretação.
Vocabulário: Tenha um bom domínio do vocabulário. Conhecer o significado das palavras ajuda muito na compreensão do texto.
"""

print(summarizer(ARTICLE, max_length=300, min_length=200, do_sample=False))
print('sleep de 3 segundos')
time.sleep(3)
print(summarizer(ARTICLE2, max_length=300, min_length=200, do_sample=False))
