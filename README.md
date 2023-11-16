# Digital Signal Processing Package

&nbsp; The [DSP package](https://github.com/mrmalvicino/dsp) provides a set of tools for digital signal processing in Python. It is designed to facilitate the generation, manipulation, and visualization of signals, as well as the application of filters and signals processing.

## Features

&nbsp; This package pretends to simplify signal processing by alowing the user to manipulate signals as objects.

&nbsp; One of the main advantages of representing signals as objects is the clarity and simplicity of code expression. Encapsulating the signal logic in an object makes the code easier to understand because the object's methods and attributes directly reflect the properties and operations associated with the signal, eliminating the need to manage time and amplitude arrays separately.

&nbsp; Additionally, this methodology promotes code reuse. By defining signals as objects, generic classes can be created that cover a variety of common signals, allowing users to simply instantiate and adjust parameters to their specific needs. This reduces redundancy in the code and encourages modular and clean programming.

&nbsp; Another key advantage lies in the abstraction of complexity. By treating signals as objects, the internal details of their implementation can be hidden from the user, who can focus on using more intuitive methods and attributes without worrying about technical details. This simplifies the workflow and facilitates collaboration, as different users can interact with the signals consistently.

### Signal Module

&nbsp; Signal is the core class of the package, representing a signal in both the time and frequency domain. It allows manipulation of attributes such as fundamental frequency, amplitude, phase, and provides methods to load spectrums from files and modify the signal duration.

### Generator Module

&nbsp; The Generator class is used to create and combine signals. It offers methods to generate sinusoidal waves, unit impulses, and more. It also allows the summation of signals, creating new combinations of waveforms.

### Grapher Module

&nbsp; The Grapher class handles signal visualization. It provides methods to plot waveforms, frequency spectrum, and visualize multiple signals clearly.

## Documentation

&nbsp; The package [documentation](https://mrmalvicino.github.io/dsp/documentation/html/index.html) provides the necessary information to either use the software or contribute developing.
All contributions that use the following [conventions](https://github.com/mrmalvicino/dsp/blob/main/documentation/CONTRIBUTING.md) are welcome.
Visit the [change log](https://github.com/mrmalvicino/dsp/blob/main/documentation/CHANGELOG.md) for more details about the development process and future implementations.

## License

&nbsp; This is an open source project developed under the GNU General Public License. See the [LICENSE](https://github.com/mrmalvicino/dsp/blob/main/LICENSE) file for more details.