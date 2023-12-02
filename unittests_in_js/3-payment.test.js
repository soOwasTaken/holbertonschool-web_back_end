const sinon = require("sinon");
const assert = require("chai").assert;
const sendPaymentRequestToApi = require("./3-payment");
const Utils = require("./utils");

describe("sendPaymentRequestToApi", () => {
  it("should call Utils.calculateNumber with correct arguments", () => {
    const spy = sinon.spy(Utils, "calculateNumber");
    sendPaymentRequestToApi(100, 20);

    assert(spy.calledWith("SUM", 100, 20));
    assert(spy.returned(120));

    spy.restore();
  });
});
