

import pygame
import random

from player import *
from colliders import *
from platform import *
from bullet import *



# --- Sprite lists

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# List of each block in the game
block_list = pygame.sprite.Group()
collect_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    fakeplatform_list=None
    enemy_list = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.fakeplatform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        WHITE     = (   255,   255, 255)
        screen.fill(WHITE)
        #self.background = pygame.image.load("mainbackground.jpg").convert()
        #screen.blit(self.background,(self.world_shift // 3,0))
        #WHY IS IT RUNNING SO CLOW?? COMMENT OUT TOP 2 LINES, and runs great...

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.fakeplatform_list:
            platform.rect.x += shift_x

        for block in block_list:
            block.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        #self.background = pygame.image.load("background_01.png").convert()
        #WHITE    = ( 255, 255, 255)
        #self.background.set_colorkey(WHITE)
        #self.level_limit = -2500

        # Array with width, height, x, and y of platform
        level = [ [210, 70, 500, 500],
                  [210, 70, 800, 400],
                  [210, 70, 1000, 500],
                  [210, 70, 1120, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


# Loop to create enemies:
#create 5 sprites
        for i in range(10):
    # This represents a block
            block = Collect(30, 20, 15)

    # Set a random location for the block
            screen_width=1500
            screen_height=800
            block.rect.x = random.randrange(screen_width-20)
            block.rect.y = random.randrange(screen_height-90)



    # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)


# Loop to create fake platforms:
#create 5 sprites
        for i in range(8):
    # This represents a block
            block = Mt_Dew(80, 150, 65)

    # Set a random location for the block
            screen_width=3500
            screen_height=800
            block.rect.x = random.randrange(screen_width-20)#make not random later, shape as water/spikes etc/make FALSE
            block.rect.y = random.randrange(screen_height-20)


    # Add the block to the list of objects
            #block_list.add(block)#if not added, no collision detection, but z-index-top, would be good for tube to next level
            #covering a platform, so it seems as if the tube IS a platform.
            all_sprites_list.add(block)
            self.fakeplatform_list.add(block)
            collect_list.add(block)





# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [210, 30, 450, 570],
                  [210, 30, 850, 420],
                  [210, 30, 1000, 520],
                  [210, 30, 1120, 280],
                  ]


        # Go through the array above and add platforms

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)



def main():
    """ Main Program """
    pygame.init()

    SCREEN_WIDTH  = 1300
    SCREEN_HEIGHT = 600
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    BLUE     = (   0,   0, 255)
    RED      = ( 255,   0,   0)
    GREEN    = (   0, 255,   0)

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Flappy Bruce")

    # Create the player
    player = Player()
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    score=5

    # Create all the levels
    level_list = []
    level_list.append( Level_01(player) )
    level_list.append( Level_02(player) )

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    pygame.display.flip()


                if event.key == pygame.K_RIGHT:
                    player.go_right()
                    pygame.display.flip()

                if event.key == pygame.K_UP:
                    player.jump()

                if event.key == pygame.K_1:
                # Fire a bullet
                    bullet = Bullet_left()
                # Set the bullet so it is where the player is
                    bullet.rect.x = player.rect.x+50
                    bullet.rect.y = player.rect.y+64
                # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

                if event.key == pygame.K_2:
                # Fire a bullet
                    bullet = Bullet_up()
                # Set the bullet so it is where the player is
                    bullet.rect.x = player.rect.x+50
                    bullet.rect.y = player.rect.y+64
                # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                if event.key == pygame.K_3:
                # Fire a bullet
                    bullet = Bullet_right()
                # Set the bullet so it is where the player is
                    bullet.rect.x = player.rect.x+50
                    bullet.rect.y = player.rect.y+64
                # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()


        # Update the player.
        active_sprite_list.update()
        all_sprites_list.update()

        # Calculate mechanics for each bullet
        for bullet in bullet_list:

            # See if it hit a block
            enemy_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
            dew_list = pygame.sprite.spritecollide(bullet, collect_list, True)
            #(bullet, target, true to disappear when hits something)

        # For each block hit, remove the bullet and add to the score
            for block in enemy_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1  #adds to score if bullet hits bloack
                print(score)

        # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)


        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

    # See if the player block has collided with anything.
    #spritecollide function:
    # true will make it REMOVE THE BLOCK HIT, false will not
        enemy_hit_list = pygame.sprite.spritecollide(player,block_list,True)
        dew_list = pygame.sprite.spritecollide(player,collect_list,True)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
                # Draw all the spites
        all_sprites_list.draw(screen)

        for block in enemy_hit_list:
            score -=1 #removes from score if touch block, bullet will add to score
            print(score)
        for block in dew_list:
            score +=5
            print(score)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(player.name)+"'s SCORE: "+str(score),15, (BLACK))
        screen.blit(label, (100, 100))

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close the program when the user hits exit:
    pygame.quit ()

if __name__ == "__main__":
    main()