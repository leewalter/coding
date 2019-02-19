// nodejs to compose my FIRST song with code !
// Walter-song1 based on https://github.com/scribbletune/scribbletune/blob/master/examples/bassline.js
// npm install scribbletune


'use strict';

// include scribbletunes sources *.js, e.g. clip.js, scale.js, utils.jsm etc..
const scribble = require('../src/');

// Get alternate notes from the C Phrygian mode
var notes1 = scribble.scale('C2 phrygian').filter((x, i) => i % 2 === 1);
// console.log(notes1);
// debug - [ 'Db2', 'F2', 'Ab2' ]

// Get alternate notes from the C4 Major mode
var notes2 = scribble.scale('c4 major').filter((x, i) => i % 2 === 0);
// console.log(notes2);
// debug - [ 'C4', 'E4', 'G4', 'B4' ]

var notes3 = notes2.concat(notes1)
// debug - [ 'C4', 'E4', 'G4', 'B4', 'Db2', 'F2', 'Ab2' ]

// Generate 4 clips (one for each note) and concat them together
var clip = notes3.reduce((accumulator, note) => {
	return accumulator.concat(scribble.clip({
		notes: [note],
		pattern: 'x-x_-xx_'.repeat(4), // Each note will use this pattern; x is on, _ is off, - is hold
		subdiv: '16n' // use a 16th note as the default duration of a note
	}));
}, []);

// Export a midi file from this clip
scribble.midi(clip, 'Walter-song1.mid');

// This will create a file called music.mid in the same location as you run this script
// Import this file in a music production software and play it with a bass synth

// this song can be listened at 
// https://soundcloud.com/user-894977529/walter-song1-composed-with-nodejs-code
