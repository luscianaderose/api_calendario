# APLICAÇÃO DA RECEPÇÃO DE CÂMARAS DA CEFP: API CALENDÁRIO

## OBJETIVO DA APLICAÇÃO

A Congregação Espírita Francisco de Paula oferece tratamentos espirituais de passe nas reuniões públicas. Após comparecer por doze semanas, os frequentadores podem marcar os serviços de vidência e prece. Na vidência, o médium fala sobre o frequentador. Na prece, o frequentador escolhe dois desencarnados e recebe informações deles através do médium. Cada atividade é feita em uma pequena câmara. Na sexta-feira, existem quatro câmaras funcionando: duas de vidência e duas de prece. O frequentador se apresenta à recepção e entra na fila. Existe uma fila única para as duas câmaras de vidência e outra fila única par as duas câmaras de prece. Quando começam os trabalhos, o recepcionista começa a chamar os nomes pela ordem de chegada. A câmara toca uma campaínha avisando que está disponível para chamar o próximo frequentador. O problema é que o recepcionista não consegue identificar qual câmara tocou a campaínha e o som é muito alto atrapalhando a concentração dos trabalhos, por vezes até assustando as pessoas. Esta aplicação tem o objetivo de melhorar a eficiência e a tranquilidade da recepção mostrando em um monitor na sala de espera o nome da pessoa e a câmara que está chamando. A aplicação substituirá o som da campaínha por um som de uma voz em volume adequado dizendo qual câmara está chamando. Estamos trabalhando para que em breve haja um botão físico em cada câmara que se conectará ao programa e chamará o próximo a ser atendido diretamente no monitor da sala de espera. Para mais informações sobre a CEFP acesse cefp.org.br.

A API fornece um calendário completo, incluindo feriados, para um ano ou mês específico. Para isso, ela integra a [`Brasil API`](https://brasilapi.com.br/docs#tag/Feriados-Nacionais), que oferece dados sobre feriados existentes apenas por ano, mas não disponibiliza o calendário completo. Esta API preenche essa lacuna, permitindo que os usuários acessem um calendário abrangente com todas as datas relevantes.

## SUMÁRIO

- [`INSTALAÇÃO`](#INSTALAÇÃO)
- [`API EXTERNA`](#API-EXTERNA)
- [`LINKS DO PROJETO`](#LINKS-DO-PROJETO)

## INSTALAÇÃO

### PRÉ-REQUISITOS

- Instalar o Docker na máquina

### PARA INICIAR A API CALENDÁRIO

Digite os seguintes comandos no terminal:

```
git clone https://github.com/luscianaderose/api_calendario
docker build -t nome_da_imagem .
docker run -d -p 5000:5000 nome_da_imagem
```

Para acessar no navegador:
http://localhost:5000/

## API EXTERNA

A api externa é a Brasil API que fornece informações gerais sobre o Brasil como mapeadomento de CEP ou feriados.

Sobre a API:

- `Documentação`: https://brasilapi.com.br/docs
- `Licença`: Licença MIT
- ``Cadastro`: Não aplicável

Rotas Utilizadas:

- `Documentação`: https://brasilapi.com.br/docs#tag/Feriados-Nacionais
- `https://brasilapi.com.br/api/feriados/v1/{ano}`: retorna todos os feriados por ano

## LINKS DO PROJETO

Os demais repositórios associados a este projetos podem ser consultados em:

- [api_recepcao](https://github.com/luscianaderose/api_recepcao)
- [api_calendario](https://github.com/luscianaderose/api_calendario)
- [front_recepcao](https://github.com/luscianaderose/front_recepcao)
- [figma](https://www.figma.com/proto/4WaxuFjrOhR8aIHIlHXuIP/prj-recepcao-cefp-01?node-id=0-1&t=XGYyK7bsqyAa5qK2-1)
