from code.Const import SCREEN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_screen(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0
        if isinstance(entity, PlayerShot):
            if entity.rect.left >= SCREEN_WIDTH:
                entity.health = 0
        if isinstance(entity, EnemyShot):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            receiving_each_entity = entity_list[i]
            EntityMediator.__verify_collision_screen(receiving_each_entity)
            for j in range(i + 1, len(entity_list)):
                receiving_each_entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(receiving_each_entity, receiving_each_entity2)

    @staticmethod
    def __verify_collision_entity(receiving_each_entity, receiving_each_entity2):
        validator_interactions = False
        if isinstance(receiving_each_entity, Enemy) and isinstance(receiving_each_entity2, PlayerShot):
            validator_interactions = True
        elif isinstance(receiving_each_entity, PlayerShot) and isinstance(receiving_each_entity2, Enemy):
            validator_interactions = True
        elif isinstance(receiving_each_entity, Player) and isinstance(receiving_each_entity2, EnemyShot):
            validator_interactions = True
        elif isinstance(receiving_each_entity, EnemyShot) and isinstance(receiving_each_entity2, Player):
            validator_interactions = True

        if validator_interactions:
            if (receiving_each_entity.rect.right >= receiving_each_entity2.rect.left and
                    receiving_each_entity.rect.left <= receiving_each_entity2.rect.right and
                    receiving_each_entity.rect.bottom >= receiving_each_entity2.rect.top and
                    receiving_each_entity.rect.top <= receiving_each_entity2.rect.bottom):
                receiving_each_entity.health -= receiving_each_entity2.damage
                receiving_each_entity2.health -= receiving_each_entity.damage
                receiving_each_entity.last_dmg = receiving_each_entity2.name
                receiving_each_entity2.last_dmg = receiving_each_entity.name