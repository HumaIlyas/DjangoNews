/**
 * @jest-environment jsdom
 */

const {setTimeout} = require("../message");

it('should set alert to "close" after 2980ms when close is fired', (done) => {
    setTimeout(() => {
        expect(alert.close);
        done();
      }, 3000);
    });