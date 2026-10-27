
# Registro do ciclo de TDD

## Comportamento escolhido

Implementar a função `calcular_taxa_entrega(distancia_km, total_pedido)`, responsável por calcular a taxa de entrega de acordo com a distância percorrida e o valor total do pedido.

As regras definidas são:
- Para distâncias de até 3 km, a taxa é de R$ 5,00.
- Para distâncias acima de 3 km, são acrescentados R$ 2,00 por quilômetro excedente.
- Para pedidos com valor igual ou superior a R$ 100,00, a entrega é gratuita.

## Red

**Teste criado:** `test_calcular_taxa_entrega_ate_3_km`, `test_calcular_taxa_entrega_acima_de_3_km` e `test_calcular_taxa_entrega_gratis_pedido_a_partir_de_100`.

**Motivo da falha:** Inicialmente, a função retornava apenas R$ 5,00, independentemente da distância ou do valor do pedido. Por isso, o teste para distâncias acima de 3 km falhou. A regra de entrega gratuita também ainda não estava implementada.

## Green

**Implementação realizada:** A função foi implementada para retornar R$ 5,00 em distâncias de até 3 km, acrescentar R$ 2,00 por quilômetro excedente e retornar R$ 0,00 quando o pedido for igual ou superior a R$ 100,00.

## Refactor

**Melhoria realizada:** A função foi organizada com condições separadas para cada regra de negócio, priorizando a verificação de entrega gratuita antes do cálculo da taxa por distância. Não foi necessária nenhuma outra alteração estrutural.

**Resultado final:** Após a implementação, todos os 7 testes automatizados foram aprovados, incluindo os 4 testes originais de cálculo e validação de pedidos e os 3 testes da taxa de entrega.
