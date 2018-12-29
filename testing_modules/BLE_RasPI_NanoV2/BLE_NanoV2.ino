/*
 * Sends 3 values of counter - past, present, future using UART BLE service
 */

#include <nRF5x_BLE_API.h>

#define DEVICE_NAME "BLE_Peripheral"
#define TXRX_BUF_LEN 4

BLE ble;
Timeout timeout;

static uint8_t rx_buf[TXRX_BUF_LEN];
static uint8_t rx_buf_num;
static uint16_t counter;

static const uint8_t service1_uuid[]        = {0x71, 0x3D, 0, 1, 0x50, 0x3E, 0x4C, 0x75, 0xBA, 0x94, 0x31, 0x48, 0xF1, 0x8D, 0x94, 0x1E};
static const uint8_t service1_tx_uuid[]     = {0x71, 0x3D, 0, 3, 0x50, 0x3E, 0x4C, 0x75, 0xBA, 0x94, 0x31, 0x48, 0xF1, 0x8D, 0x94, 0x1E};
static const uint8_t service1_rx_uuid[]     = {0x71, 0x3D, 0, 2, 0x50, 0x3E, 0x4C, 0x75, 0xBA, 0x94, 0x31, 0x48, 0xF1, 0x8D, 0x94, 0x1E};
static const uint8_t uart_base_uuid_rev[]   = {0x1E, 0x94, 0x8D, 0xF1, 0x48, 0x31, 0x94, 0xBA, 0x75, 0x4C, 0x3E, 0x50, 0, 0, 0x3D, 0x71};

uint8_t tx_value[TXRX_BUF_LEN] = {0,};
uint8_t rx_value[TXRX_BUF_LEN] = {0,};

GattCharacteristic  characteristic1(service1_tx_uuid, tx_value, 1, TXRX_BUF_LEN, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_WRITE | GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_WRITE_WITHOUT_RESPONSE );
GattCharacteristic  characteristic2(service1_rx_uuid, rx_value, 1, TXRX_BUF_LEN, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY);
GattCharacteristic *uartChars[] = {&characteristic1, &characteristic2};
GattService         uartService(service1_uuid, uartChars, sizeof(uartChars) / sizeof(GattCharacteristic *));

void disconnectionCallBack(const Gap::DisconnectionCallbackParams_t *params) {
  ble.startAdvertising();
}

void increase_counter() {
    rx_buf_num = 4;

    if (counter > 256) {
      counter = 0;
    }

    rx_buf[0] = rx_buf_num - 1; // number of items
    rx_buf[1] = counter++; // past
    rx_buf[2] = counter;   // present
    rx_buf[3] = counter + 1; // future

    ble.updateCharacteristicValue(characteristic2.getValueAttribute().getHandle(), rx_buf, rx_buf_num);
    memset(rx_buf, 0x00, TXRX_BUF_LEN);
    rx_buf_num = 0;

    timeout.attach_us(increase_counter, 1000000);
}

void setup() {
  counter = 0;
  timeout.attach_us(increase_counter, 1000000); // the time here is in micro-seconds

  ble.init();
  ble.onDisconnection(disconnectionCallBack);

  // setup adv_data and srp_data
  ble.accumulateAdvertisingPayload(GapAdvertisingData::BREDR_NOT_SUPPORTED);
  ble.accumulateAdvertisingPayload(GapAdvertisingData::SHORTENED_LOCAL_NAME,
                                   (const uint8_t *)"TXRX", sizeof("TXRX") - 1);
  ble.accumulateAdvertisingPayload(GapAdvertisingData::COMPLETE_LIST_128BIT_SERVICE_IDS,
                                   (const uint8_t *)uart_base_uuid_rev, sizeof(uart_base_uuid_rev));
  // set adv_type
  ble.setAdvertisingType(GapAdvertisingParams::ADV_CONNECTABLE_UNDIRECTED);
  // add service
  ble.addService(uartService);
  // set device name
  ble.setDeviceName((const uint8_t *)DEVICE_NAME);
  // set tx power,valid values are -40, -20, -16, -12, -8, -4, 0, 4
  ble.setTxPower(4);
  // set adv_interval, 100ms in multiples of 0.625ms.
  ble.setAdvertisingInterval(160);
  // set adv_timeout, in seconds
  ble.setAdvertisingTimeout(0);
  // start advertising
  ble.startAdvertising();
}

void loop() {
    ble.waitForEvent();
}
