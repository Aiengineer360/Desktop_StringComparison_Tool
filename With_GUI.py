import sys
import string
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QTextEdit, QPushButton, QLabel, QTabWidget, QGroupBox)
from PyQt5.QtCore import Qt


class StringComparisonTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("String Comparison Tool")
        self.setGeometry(100, 100, 900, 700)

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        # Initialize UI
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface components."""
        # Create tab widget
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        # Add tabs
        self.add_input_tab()
        self.add_comparison_tab()
        self.add_word_count_tab()

        # Status bar
        self.status_bar = self.statusBar()

    def add_input_tab(self):
        """Add the input tab with text areas."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # String 1 input
        group1 = QGroupBox("String 1")
        layout1 = QVBoxLayout()
        self.text_edit1 = QTextEdit()
        self.text_edit1.setPlaceholderText("Enter first string here...")
        layout1.addWidget(self.text_edit1)
        group1.setLayout(layout1)

        # String 2 input
        group2 = QGroupBox("String 2")
        layout2 = QVBoxLayout()
        self.text_edit2 = QTextEdit()
        self.text_edit2.setPlaceholderText("Enter second string here...")
        layout2.addWidget(self.text_edit2)
        group2.setLayout(layout2)

        # Add groups to layout
        layout.addWidget(group1)
        layout.addWidget(group2)

        # Preprocess button
        self.preprocess_btn = QPushButton("Preprocess Strings")
        self.preprocess_btn.clicked.connect(self.preprocess_strings)
        layout.addWidget(self.preprocess_btn)

        self.tabs.addTab(tab, "Input")

    def add_comparison_tab(self):
        """Add the comparison methods tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Comparison methods group
        group = QGroupBox("Comparison Methods")
        group_layout = QVBoxLayout()

        # Split method
        self.split_btn = QPushButton("Compare Using Word Split")
        self.split_btn.clicked.connect(self.compare_using_split)
        group_layout.addWidget(self.split_btn)

        # Interning method
        self.interning_btn = QPushButton("Compare Using String Interning")
        self.interning_btn.clicked.connect(self.compare_using_interning)
        group_layout.addWidget(self.interning_btn)

        # Results label
        self.comparison_result = QLabel("Results will appear here...")
        self.comparison_result.setWordWrap(True)
        self.comparison_result.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        group_layout.addWidget(self.comparison_result)

        group.setLayout(group_layout)
        layout.addWidget(group)

        # Performance comparison
        perf_group = QGroupBox("Performance Comparison")
        perf_layout = QVBoxLayout()

        self.compare_methods_btn = QPushButton("Compare Both Methods")
        self.compare_methods_btn.clicked.connect(self.compare_methods_performance)
        perf_layout.addWidget(self.compare_methods_btn)

        self.performance_result = QLabel("Performance results will appear here...")
        self.performance_result.setWordWrap(True)
        perf_layout.addWidget(self.performance_result)

        perf_group.setLayout(perf_layout)
        layout.addWidget(perf_group)

        self.tabs.addTab(tab, "Comparison")

    def add_word_count_tab(self):
        """Add the word count analysis tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Word count buttons
        btn_layout = QHBoxLayout()
        self.count_words_btn1 = QPushButton("Count Words in String 1")
        self.count_words_btn1.clicked.connect(lambda: self.count_words(1))
        btn_layout.addWidget(self.count_words_btn1)

        self.count_words_btn2 = QPushButton("Count Words in String 2")
        self.count_words_btn2.clicked.connect(lambda: self.count_words(2))
        btn_layout.addWidget(self.count_words_btn2)

        self.compare_counts_btn = QPushButton("Compare Word Counts")
        self.compare_counts_btn.clicked.connect(self.compare_word_counts)
        btn_layout.addWidget(self.compare_counts_btn)

        layout.addLayout(btn_layout)

        # Word count results
        self.word_count_result = QTextEdit()
        self.word_count_result.setReadOnly(True)
        self.word_count_result.setPlaceholderText("Word count results will appear here...")
        layout.addWidget(self.word_count_result)

        self.tabs.addTab(tab, "Word Analysis")

    def preprocess_strings(self):
        """Preprocess both input strings."""
        string1 = self.text_edit1.toPlainText()
        string2 = self.text_edit2.toPlainText()

        if not string1 or not string2:
            self.status_bar.showMessage("Both strings must contain text!", 3000)
            return

        self.processed1 = self.preprocess_string(string1)
        self.processed2 = self.preprocess_string(string2)

        self.status_bar.showMessage("Strings preprocessed successfully!", 3000)

    def preprocess_string(self, input_string):
        """Remove all non-alphabetic characters and extra spaces from the string."""
        processed_chars = []
        prev_char = ""

        for char in input_string:
            if char in string.ascii_letters:
                processed_chars.append(char)
                prev_char = char
            elif prev_char != " ":
                processed_chars.append(" ")
                prev_char = " "

        return "".join(processed_chars)

    def compare_using_split(self):
        """Compare strings by splitting into words."""
        if not hasattr(self, 'processed1') or not hasattr(self, 'processed2'):
            self.status_bar.showMessage("Please preprocess strings first!", 3000)
            return

        start = time.perf_counter()
        words1 = self.processed1.split()
        words2 = self.processed2.split()

        result = "-------- Word Comparison Using Split --------\n"
        if words1 == words2:
            result += "String 1 == String 2\n"
        else:
            result += "String 1 != String 2\n"

        elapsed = time.perf_counter() - start
        result += f"\nComparison took {elapsed:.6f} seconds"

        self.comparison_result.setText(result)
        self.status_bar.showMessage("Word split comparison completed!", 3000)

    def compare_using_interning(self):
        """Compare strings using string interning."""
        if not hasattr(self, 'processed1') or not hasattr(self, 'processed2'):
            self.status_bar.showMessage("Please preprocess strings first!", 3000)
            return

        start = time.perf_counter()
        interned1 = sys.intern(self.processed1)
        interned2 = sys.intern(self.processed2)

        result = "-------- Comparison Using String Interning --------\n"
        if interned1 is interned2:
            result += "String 1 == String 2\n"
            result += f"String 1 ID: {hex(id(interned1))} == String 2 ID: {hex(id(interned2))}\n"
        else:
            result += "String 1 != String 2\n"
            result += f"String 1 ID: {hex(id(interned1))} != String 2 ID: {hex(id(interned2))}\n"

        elapsed = time.perf_counter() - start
        result += f"\nComparison took {elapsed:.6f} seconds"

        self.comparison_result.setText(result)
        self.status_bar.showMessage("Interning comparison completed!", 3000)

    def compare_methods_performance(self):
        """Compare performance of both comparison methods."""
        if not hasattr(self, 'processed1') or not hasattr(self, 'processed2'):
            self.status_bar.showMessage("Please preprocess strings first!", 3000)
            return

        # Create larger strings for better performance measurement
        large1 = self.processed1 * 100
        large2 = self.processed2 * 100

        # Time split method
        start_split = time.perf_counter()
        words1 = large1.split()
        words2 = large2.split()
        words1 == words2  # Perform comparison
        split_time = time.perf_counter() - start_split

        # Time interning method
        start_interning = time.perf_counter()
        interned1 = sys.intern(large1)
        interned2 = sys.intern(large2)
        interned1 is interned2  # Perform comparison
        interning_time = time.perf_counter() - start_interning

        # Display results
        result = "-------- Performance Comparison --------\n"
        result += f"Split method time: {split_time:.6f} seconds\n"
        result += f"Interning method time: {interning_time:.6f} seconds\n\n"

        if split_time > interning_time:
            result += "Word-by-word comparison was slower than interning method"
        else:
            result += "Word-by-word comparison was faster than interning method"

        self.performance_result.setText(result)
        self.status_bar.showMessage("Performance comparison completed!", 3000)

    def count_words(self, string_num):
        """Count words in the specified string (1 or 2)."""
        if not hasattr(self, 'processed1') or not hasattr(self, 'processed2'):
            self.status_bar.showMessage("Please preprocess strings first!", 3000)
            return

        input_string = self.processed1 if string_num == 1 else self.processed2
        word_counts = self._count_words(input_string)

        # Format the output
        result = f"-------- Word Count for String {string_num} --------\n"
        for word, count in sorted(word_counts.items()):
            result += f"'{word}': {count}\n"

        self.word_count_result.setText(result)
        self.status_bar.showMessage(f"Word count for String {string_num} completed!", 3000)

    def _count_words(self, input_string):
        """Count word occurrences in string and return as dictionary."""
        words = input_string.split()
        word_counts = {}

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        return word_counts

    def compare_word_counts(self):
        """Compare word counts between both strings."""
        if not hasattr(self, 'processed1') or not hasattr(self, 'processed2'):
            self.status_bar.showMessage("Please preprocess strings first!", 3000)
            return

        start = time.perf_counter()
        counts1 = self._count_words(self.processed1)
        counts2 = self._count_words(self.processed2)

        result = "-------- Word Count Comparison --------\n"
        if counts1 == counts2:
            result += "Word counts match\n"
        else:
            result += "Word counts differ\n"

        elapsed = time.perf_counter() - start
        result += f"\nComparison took {elapsed:.6f} seconds"

        self.word_count_result.setText(result)
        self.status_bar.showMessage("Word count comparison completed!", 3000)


def main():
    app = QApplication(sys.argv)
    window = StringComparisonTool()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()