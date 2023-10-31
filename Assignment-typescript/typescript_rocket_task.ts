interface Payload {
    massKg: number;
}

class Astronaut implements Payload {
    massKg: number;
    name: string;

    constructor(massKg: number, name: string) {
        this.massKg = massKg;
        this.name = name;
    }
}

class Cargo implements Payload {
    massKg: number;
    material: string;

    constructor(massKg: number, material: string) {
        this.massKg = massKg;
        this.material = material;
    }
}

class Rocket {
    name: string;
    totalCapacityKg: number;
    cargoItems: Cargo[] = [];
    astronauts: Astronaut[] = [];

    constructor(name: string, totalCapacityKg: number) {
        this.name = name;
        this.totalCapacityKg = totalCapacityKg;
    }

    sumMass(items: Payload[]): number {
        return items.reduce((total, item) => total + item.massKg, 0);
    }

    currentMassKg(): number {
        return this.sumMass(this.cargoItems) + this.sumMass(this.astronauts);
    }

    canAdd(item: Payload): boolean {
        let massKg = this.currentMassKg() + item.massKg;
        return massKg <= this.totalCapacityKg;
    }

    addCargo(cargo: Cargo): boolean {
        let canAdd = this.canAdd(cargo);

        if (canAdd) {
            this.cargoItems.push(cargo);
            return true;
        } else {
            return false;
        }
    }

    addAstronaut(astronaut: Astronaut): boolean {
        let canAdd = this.canAdd(astronaut);

        if (canAdd) {
            this.astronauts.push(astronaut);
            return true;
        } else {
            return false;
        }
    }
}
