import numpy as np
import matplotlib.pyplot as plt


def square_wave(t: float, f: float, amp: float = 1.0):
    return amp * np.sign(np.sin(2 * np.pi * f * t))


def fourier_series_square_wave(t: float, num_terms: int = 10):
    res: int = 0.0
    for n in range(1, num_terms + 1):
        omega = 2 * np.pi * (2 * n - 1)
        res += (4 / (np.pi * (2 * n - 1))) * np.sin(omega * t)
    return res


if __name__ == "__main__":
    # Time vector
    t = np.linspace(0, 2, 1000, endpoint=False)

    # Generate a square wave
    square_wave_values = square_wave(t, f=1)

    # Calculate the Fourier series approx.
    num_terms = 10
    fourier_approx = fourier_series_square_wave(t, num_terms)

    # Plotting the square wave and its Fourier series approx.
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, square_wave_values, label='Square Wave')
    plt.title('Original Square Wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(t,
             fourier_approx,
             label=f'Fourier Series (terms={num_terms})',
             linestyle='--')
    plt.title('Fourier Series Approximation of Square Wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.tight_layout()
    plt.savefig('signals_and_systems/square_wave')
    plt.show()
