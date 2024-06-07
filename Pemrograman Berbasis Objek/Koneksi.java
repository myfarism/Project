import java.sql.Connection;
import java.sql.DriverManager; 
import javax.swing.JOptionPane;

public class Koneksi {
    private static Connection koneksi;

    public static Connection getKoneksi() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            koneksi = DriverManager.getConnection("jdbc:mysql://localhost/db_test", "root", "");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Koneksi ke Database gagal!");
        }
        return koneksi;
    }
}