from math import exp
from typing import List, Tuple


class FunctionAnalyzer:
    def __init__(self, initial_z: float, step_size: float, final_z: float):
        self.initial_z: float = initial_z
        self.step_size: float = step_size
        self.final_z: float = final_z
        self.extended_final_z: float = final_z + 0.1e-10  # Extend to include final value
        self.z_values: List[float] = []
        self.s1_values: List[float] = []
        self.s2_values: List[float] = []
        self.s1_min: float = 0.0
        self.s1_max: float = 0.0
        self.positive_s1_count: int = 0
        self.positive_s2_count: int = 0

    def calculate_functions(self) -> None:
        """
        Calculate S1 and S2 for each z and store the results.
        """
        z = self.initial_z
        while z < self.extended_final_z:
            s1 = self.calculate_s1(z)
            s2 = self.calculate_s2(z)
            self.z_values.append(z)
            self.s1_values.append(s1)
            self.s2_values.append(s2)
            z += self.step_size

    @staticmethod
    def calculate_s1(z: float) -> float:
        """
        Calculate S1 based on z.
        """
        return z**3 - 4.51 * z**2 - 23.9 * z + 20.1

    @staticmethod
    def calculate_s2(z: float) -> float:
        """
        Calculate S2 based on z.
        """
        return exp(-z) - (z - 1)**2

    def print_table(self) -> None:
        """
        Print the table of z, S1, and S2 values with appropriate formatting.
        """
        print('\nTable of Function Values:')
        print('      Z           S1             S2')
        for z, s1, s2 in zip(self.z_values, self.s1_values, self.s2_values):
            if abs(s1) >= 9999 and abs(s2) >= 9999:
                print(f'{z:10.3f}    {s1:9.2e}      {s2:9.2e}')
            elif abs(s1) >= 9999 and 0 <= abs(s2) <= 9999:
                print(f'{z:10.3f}    {s1:9.2e}      {s2:9.3f}')
            elif abs(s2) >= 9999 and 0 <= abs(s1) <= 9999:
                print(f'{z:10.3f}    {s1:9.3f}      {s2:9.2e}')
            else:
                print(f'{z:10.3f}    {s1:9.3f}      {s2:9.3f}')

    def count_positive_values(self) -> None:
        """
        Count the number of positive values in S1 and S2.
        """
        self.positive_s1_count = sum(1 for s1 in self.s1_values if s1 > 0)
        self.positive_s2_count = sum(1 for s2 in self.s2_values if s2 > 0)

    def find_s1_min_max(self) -> None:
        """
        Find the minimum and maximum values of S1.
        """
        if not self.s1_values:
            self.s1_min = 0.0
            self.s1_max = 0.0
        else:
            self.s1_min = min(self.s1_values)
            self.s1_max = max(self.s1_values)

    def print_positive_counts(self) -> None:
        """
        Print the counts of positive S1 and S2 values.
        """
        print('\nNumber of Positive Elements in Function S1:', self.positive_s1_count)
        print('Number of Positive Elements in Function S2:', self.positive_s2_count)

    def plot_graph(self) -> None:
        """
        Plot the graph of S1 with the x-axis.
        """
        if self.s1_max == self.s1_min:
            print("\nCannot plot graph because S1 has a constant value.")
            return

        graph_width = 65
        axis_position = round((-self.s1_min) / (self.s1_max - self.s1_min) * graph_width)
        has_x_axis = self.s1_max > 0 and self.s1_min < 0

        print('\nGraph of Function S1:\n')

        for z, s1 in zip(self.z_values, self.s1_values):
            scaled_position = int((s1 - self.s1_min) / (self.s1_max - self.s1_min) * graph_width)
            line = f'{z:9.3f} '

            for i in range(graph_width + 1):
                if i == scaled_position and i == axis_position and has_x_axis:
                    line += '+'  # Intersection point
                elif i == scaled_position:
                    line += '*'  # S1 point
                elif i == axis_position and has_x_axis:
                    line += '|'  # X-axis
                else:
                    line += ' '  # Empty space
            print(line)

    def run_analysis(self) -> None:
        """
        Run the full analysis: calculate functions, print table, count positives, and plot graph.
        """
        self.calculate_functions()
        self.print_table()
        self.count_positive_values()
        self.print_positive_counts()
        self.find_s1_min_max()
        self.plot_graph()


def get_user_input() -> Tuple[float, float, float]:
    """
    Get initial value, step size, and final value from the user.
    """
    initial_z = float(input('Enter the initial value of the variable: '))
    step_size = float(input('Enter the step size for the variable: '))
    final_z = float(input('Enter the final value of the variable: '))
    return initial_z, step_size, final_z


def main() -> None:
    initial_z, step_size, final_z = get_user_input()
    analyzer = FunctionAnalyzer(initial_z, step_size, final_z)
    analyzer.run_analysis()
    input('\nPress Enter to exit...')  # Pause the program to view the output


if __name__ == '__main__':
    main()