class Scene2 extends Phaser.Scene {
    constructor(){
        super('playGame');
    }

    preload() {
        this.load.tilemapTiledJSON('map', 'assets/map.json');
        // tiles in spritesheet 
        this.load.spritesheet('tiles', 'assets/tiles.png', {frameWidth: 70, frameHeight: 70});
        // player animations
        this.load.atlas('player', 'assets/player.png', 'assets/player.json');
    }


    create(){

        // load the map 
        map = this.make.tilemap({key: 'map'});
    
        // tiles for the ground layer
        var groundTiles = map.addTilesetImage('tiles');
        // create the ground layer
        groundLayer = map.createDynamicLayer('World', groundTiles, 0, 0);
        // the player will collide with this layer
        groundLayer.setCollisionByExclusion([-1]);
    
        // set the boundaries of our game world
        this.physics.world.bounds.width = groundLayer.width;
        this.physics.world.bounds.height = groundLayer.height;

        player = this.physics.add.sprite(200, 200, 'player');
        player.setBounce(0.2); // our player will bounce from items
        player.setCollideWorldBounds(true); // don't go out of the map

        this.cameras.main.startFollow(player)
    
        // player will collide with the level tiles
        this.physics.add.collider(groundLayer, player);

        // player walk animation
        this.anims.create({
            key: 'walk',
            frames: this.anims.generateFrameNames('player', {prefix: 'p1_walk', start: 1, end: 0, zeroPad: 2}),
            frameRate: 10,
            repeat: -1
        });
        // player jumps animation
        this.anims.create({
            key: 'jump',
            frames: [{key: 'player', frame: 'p1_jump'}],
            frameRate: 10,
            repeat:-1
        });


        // idle with only one frame, so repeat is not neaded
        this.anims.create({
            key: 'idle',
            frames: [{key: 'player', frame: 'p1_stand'}],
            frameRate: 10,
        });

        cursors = this.input.keyboard.createCursorKeys();

        // set bounds so the camera won't go outside the game world
        this.cameras.main.setBounds(0, 0, map.widthInPixels, map.heightInPixels);
        // make the camera follow the player
        this.cameras.main.startFollow(player);

    }

    update(time, delta){

        if (cursors.left.isDown){
            player.body.setVelocityX(-200); // move left
            player.anims.play('walk', true); // play walk animation
            player.flipX= true; // flip the sprite to the left
        }
        else if (cursors.right.isDown){
            player.body.setVelocityX(200); // move right
            player.anims.play('walk', true); // play walk animatio
            player.flipX = false; // use the original sprite looking to the right
        }
        else if (cursors.up.isDown){
            player.body.setVelocityY(-270);
            player.anims.play('jump',true)
            player.flipX = false;
        }
        else {
            player.body.setVelocityX(0);
            player.anims.play('idle', true);
        }
    }

}