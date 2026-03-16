import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginForm {

    // JFrame for the login form
    private JFrame frame;
    private JTextField usernameField;
    private JPasswordField passwordField;
    private JButton loginButton;
    private JLabel messageLabel;

    // Main method to run the application
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new LoginForm().createAndShowGUI();
            }
        });
    }

    // Method to create the login form GUI
    public void createAndShowGUI() {
        frame = new JFrame("Login Form");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new FlowLayout());

        // Username field
        JLabel usernameLabel = new JLabel("Username:");
        usernameField = new JTextField(20);

        // Password field
        JLabel passwordLabel = new JLabel("Password:");
        passwordField = new JPasswordField(20);

        // Login button
        loginButton = new JButton("Login");

        // Message label to display success or failure
        messageLabel = new JLabel("");
        messageLabel.setForeground(Color.RED);

        // Add components to the frame
        frame.add(usernameLabel);
        frame.add(usernameField);
        frame.add(passwordLabel);
        frame.add(passwordField);
        frame.add(loginButton);
        frame.add(messageLabel);

        // Login button action
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Get username and password
                String username = usernameField.getText();
                char[] password = passwordField.getPassword();

                // Check if credentials are valid (for example purposes, using hardcoded values)
                if ("admin".equals(username) && "password123".equals(new String(password))) {
                    messageLabel.setText("Login successful!");
                    messageLabel.setForeground(Color.GREEN);
                } else {
                    messageLabel.setText("Invalid username or password.");
                    messageLabel.setForeground(Color.RED);
                }
            }
        });

        // Show the frame
        frame.setVisible(true);
    }
}



 



 