# import pygame
# pygame.init()
# tela=pygame.display.set_mode((500,500))

# run=True
# tela.fill('MediumBlue')
# pygame.display.flip()

# while run:
#     for event in pygame.event.get():

#         if event.type==pygame.QUIT:
#             run=False
#             pygame.quit()
#     pygame.draw.rect(tela,'red,(250,250,10,10)')
#     pygame.display.flip()

    #professora

# import pygame 


pygame.init()


tela  = pygame.display.set_mode((500,500))
run = True
tela.fill('MediumBlue')



while run:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False
                  pygame.quit()
      pygame.draw.circle(tela,'red',(50,50),20)
      pygame.draw.ellipse(tela,'green',(245,400,20,70))
      # ellipse
      # circulo
      pygame.display.flip()

      import pygame 





