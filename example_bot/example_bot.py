import sc2
from sc2.ids.unit_typeid import UnitTypeId


class ExampleBot(sc2.BotAI):
    async def on_step(self, iteration):
        # On first step, send all workers to attack enemy start location
        print(self.enemy_units)

        if self.can_afford(UnitTypeId.MARINE):
            structures = self.structures.of_type([UnitTypeId.BARRACKS])
            if structures:
                structures.first.train(UnitTypeId.MARINE)

        not_queued_units = tuple(self.units.filter(lambda u: u.is_idle))
        if len(not_queued_units) >= 5:
            for unit in not_queued_units:
                unit.attack(self.enemy_start_locations[0])
