package application;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import db.DB;

public class Program {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Connection conn = null; //DB.getConnection();
		
		Statement st = null;
		ResultSet rs = null;
		
		
		
		try {
			System.out.println("Acessando o database...");
			conn = DB.getConnection();
			
			st = conn.createStatement();
			
			rs = st.executeQuery("select * from department");
			
			while(rs.next()) {
				System.out.println(rs.getInt("Id") + "," + rs.getString("Name"));
			}
			
		}
		
		catch(SQLException e) {
			e.printStackTrace();
		}
		
		finally {
			DB.closeResultSet(rs);
			DB.closeStament(st);
			System.out.println("Fechando a conexão do database...");		
			DB.closeConnection();
		
		}
		
		
		
		
		
	}

}
