# @include library(scales), para os valores em reais e com virgula
# Para ordernar os eixo x, foi necessário fazê-lo manualmente no data frame
# usp$tempo_casa <- factor(usp$tempo_casa, levels=c("0 a 5 anos", "6 a 10 anos", "11 a 20 anos", "21 a 30 anos", "mais de 30 anos", "inativo"))

library(scales)
library(grid)
library(gridExtra)
library(ggplot2)
library(ggthemes)
library(scales)

# Analisando números diretamente com ggplot2, incluindo stat summary para a mediana

salarios <- ggplot(usp) + 
  geom_jitter(aes(usp$tempo_casa, liquido, colour = tipo), alpha = .6, stat = "identity") + 
  scale_colour_manual(values = c("#f0027f","#02f073","#807279","#386cb0")) +
  scale_y_continuous(labels=dollar_format(prefix="R$", big.mark = ".")) +
  labs (x="", y = "Remuneração líquida, em R$", 
        title = "Salários na USP", 
        subtitle ="Folha de pagamento da USP em dezembro 2016, em rendimentos líquidos,\nde acordo com status e tempo de trabalho na universidade", 
        caption = "Fonte: USP",
        colour = "cargo") +
  stat_summary(aes(tempo_casa, liquido), fun.ymin=median, fun.ymax=median, fun.y=median, geom="crossbar", size = .1) 
  
