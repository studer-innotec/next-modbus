Package **nxmodbus**
=========================

Python library to access Studer-Innotec Next devices through Modbus RTU over a serial port

Prerequisites
----------------

Please read the complete documentation available on : `Studer Innotec SA`_ *-> Support -> Download Center -> Software and Updates*

Getting Started
----------------

1. Package installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ pip install nxmodbus

2. Hardware installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Connect your Next installation through a Next gateway (e.g. nx-interface) to your controller (personal computer, Raspberry Pi, etc.) using a *USB* to *RS-485* adapter

3. Serial configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This package rely on `pyserial`_ standard package, in order to use the **nxmodbus** package make sure to instantiate it like :

.. code-block:: python

    import serial

    serial_port = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_BAUDRATE, parity=serial.PARITY_EVEN, timeout=1)

- where `SERIAL_PORT_NAME` is your serial port interface, for example set it to *'COM4'* (string argument) when using *Windows* otherwise you may set it to *'/dev/ttyUSB0/'* on *Linux*
- where `SERIAL_PORT_BAUDRATE` is the baudrate used by your serial port interface (use the Nx-interface to set the serial parameter of the server)

4. Run an example from `/examples` folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to */examples* folder with a terminal and execute this script

.. code-block:: console

    $ python ex_read_param.py

Check `client file`_ to understand it.

5. Open documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open documentation from `Read The Docs`_

Warnings
----------------

- **Use** devices addresses generated into `addresses file`_
- It is strongly recommended **NOT** to spam the *Next gateway* with multiple requests. The correct way to communicate with the *Next gateway* is to send a request and to **wait** for the response before sending the next request. If no response comes from the *nxmodbus* after a delay of 1 second, we can consider that the timeout is over and another request can be send. It is also how *Modbus RTU* is intended to work.

Authors
----------------

**Studer Innotec SA** - *Initial work* - `Studer Innotec SA`_

License
----------------

This project is licensed under the MIT License - see the `LICENSE`_ file for details

.. External References:
.. _Studer Innotec SA: https://www.studer-innotec.com
.. _addresses file: https://nxmodbus.readthedocs.io/en/latest/addresses.html
.. _client file: https://nxmodbus.readthedocs.io/en/latest/client.html
.. _Read The Docs: https://nxmodbus.readthedocs.io/en/latest/index.html
.. _LICENSE: https://nxmodbus.readthedocs.io/en/latest/license.html
.. _pyserial: https://pyserial.readthedocs.io/en/latest/shortintro.html
