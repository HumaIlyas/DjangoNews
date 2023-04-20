/**
 * @jest-environment jsdom
 */

const {setTimeout} = require("../message");

it('should set alert to "close" after 3000 ms', (done) => {
    setTimeout(() => {
        expect(alert.close);
        done();
      }, 3000);
    });